from django.shortcuts import render, redirect
from .models import Profile, FollowersCount
from main.models import Post
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .forms import  SignUpForm, LoginForm, UpdateUserForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout
from .mixins import PreventLoginSignupMixin
from django.http import JsonResponse



class SignUpView(PreventLoginSignupMixin, CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/signup.html'

class LoginCustomView(PreventLoginSignupMixin, LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    success_url = reverse_lazy('blog:home')
    

    

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('user:login')



def profile(request, username):
    user_object = get_object_or_404(User, username=username)
    user_profile = Profile.objects.get(user=user_object)
    

    follower = request.user.username
    user = username

    if FollowersCount.objects.filter(follower=follower, user=user).first():
        button_text = 'unfollow'
    else:
        button_text = 'follow'

    user_followers = len(FollowersCount.objects.filter(user=username))
    user_following = len(FollowersCount.objects.filter(follower=username))

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'button_text': button_text,
        'user_followers': user_followers,
        'user_following': user_following,
    }
    return render(request, 'user/profile.html', context)


@login_required(login_url='user:login')
def edit_profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user)
    if request.user == user:
        if request.method == "POST":
            u_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)
            p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, "your account has been updated successfully! you will now be redirected to your profile page")
                return redirect('user:profile', username)
        else:
            u_form = UpdateUserForm(instance=request.user)
            p_form = ProfileUpdateForm(instance=request.user.profile)
    else:
        return redirect('feed:feed')
    return render(request, 'user/edit_profile.html', {'user': user,
                                                        'user_profile': user_profile,
                                                        'u_form': u_form,
                                                        'p_form': p_form})
    
    



@login_required(login_url='user:login')
def follow(request):
    if request.method == "POST":
        follower = request.POST['follower']
        user = request.POST['user']

        if FollowersCount.objects.filter(follower=follower, user=user).exists():
            delete_follower = FollowersCount.objects.get(follower=follower, user=user)
            delete_follower.delete()
            action = 'unfollowed'
        else:
            new_follower = FollowersCount.objects.create(follower=follower, user=user)
            action = 'followed'

        response_data = {'status': 'success', 'action': action}
        return JsonResponse(response_data)
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})

 
