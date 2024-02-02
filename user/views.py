from django.shortcuts import render, redirect
from .models import Profile
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from .forms import  SignUpForm, LoginForm, UpdateUserForm, ProfileUpdateForm
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView
from django.contrib.auth import logout



class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('user:login')
    template_name = 'user/signup.html'

class LoginCustomView(LoginView):
    form_class = LoginForm
    template_name = 'user/login.html'
    

def logout_view(request):
    logout(request)
    messages.success(request, 'You have been successfully logged out.')
    return redirect('user:login')



def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_profile = get_object_or_404(Profile, user=user)


    context = {
        'user': user,
        'user_profile': user_profile,
    }
    return render(request, 'user/profile.html', context)


@login_required(login_url='account_login')
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
                messages.success(request, "your account has been updated successfully!")
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
