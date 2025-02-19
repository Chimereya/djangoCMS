from django.shortcuts import render, get_object_or_404, redirect
from django.utils.translation import gettext as _
from .models import Post, Comment
from .forms import CommentForm
from user.models import Profile
from django.contrib.auth.models import User
from django.views.generic import (
    ListView,
    DetailView,
    RedirectView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView,
    FormView,
    View
    )
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.decorators.http import require_POST
from .forms import CommentForm
from django.http import HttpResponseRedirect
from django.urls import reverse



class HomeView(TemplateView):
    model = Post
    template_name = 'main/home.html'
        
        
  
class PostListView(ListView):
    model = Post
    template_name = 'main/post_list.html'
    paginate_by = 2

    def get_queryset(self):
        return Post.objects.all()
    
    

class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail.html'
    context_object_name = 'post'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.increment_view_count()  # Increment view count
        return obj
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        context['form'] = CommentForm()
        context['is_favourite'] = post.favourite.filter(id=self.request.user.id).exists()
        return context

    def post(self, request, slug):
        post = self.get_object()
        form = CommentForm(request.POST)
        if form.is_valid():
            parent_comment_id = request.POST.get('parent_comment_id')
            parent_comment = None
            if parent_comment_id:
                parent_comment = get_object_or_404(Comment, id=parent_comment_id)
            comment = form.save(commit=False)
            comment.post = post
            comment.parent = parent_comment
            comment.author = request.user
            comment.save()
            return redirect('blog:detail', slug=slug)
        
        context = self.get_context_data(post=post, form=form)
        return self.render_to_response(context)
 
    
class PostView(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'main/manage_posts.html'
    context_object_name = 'blog_list'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Filter posts by the logged-in user and then count them
            user_post_count = Post.objects.filter(author=self.request.user).count()
            # Add user_post_count to the context
            context['user_post_count'] = user_post_count
        return context

    def get_queryset(self):
        # Filter posts by the currently logged-in user
        return Post.objects.filter(author=self.request.user)
    
    
class CreatepostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'main/create.html'
    context_object_name = 'blog_list'
    fields = ['title', 'tags', 'content', 'image', 'image_credit', 'status']
    success_url = reverse_lazy('blog:posts')
    
    def form_valid(self, form):
        # Setting the author to the current user
        form.instance.author = self.request.user  
        return super().form_valid(form)
    
    
class EditView(LoginRequiredMixin, UpdateView):
    model = Post
    template_name = 'main/edit.html'
    fields = ['title', 'tags', 'content', 'image', 'image_credit', 'status']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')
    
    def form_valid(self, form):
        # Setting the author to the current user
        form.instance.author = self.request.user  
        return super().form_valid(form)
    

class Delete(LoginRequiredMixin, DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')
    template_name = 'main/delete.html'


def user_posts(request, username):
    user = User.objects.get(username=username)
    user_profile = Profile.objects.get(user=user)
    posts = Post.objects.filter(author=user)
    return render(request, 'main/user_page.html', {'posts': posts, 'user': user, 'user_profile': user_profile})

@login_required
def like_post(request, slug):
    if request.method == 'POST' and request.headers.get('x-requested-with') == 'XMLHttpRequest':
        post = get_object_or_404(Post, slug=slug)
        user = request.user

        if user in post.likes.all():
            post.likes.remove(user)
            liked = False
        else:
            post.likes.add(user)
            liked = True

        post.save()

        return JsonResponse({'liked': liked, 'count': post.likes.count()})
    else:
        return JsonResponse({'error': _('Invalid request')}, status=400)

    
def favourite_post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if post.favourite.filter(id=request.user.id).exists():
        post.favourite.remove(request.user)
        is_favourite = False
    else:
        post.favourite.add(request.user)
        is_favourite = True

    # Redirect to the post detail page after toggling favorite status
    return redirect('blog:detail', slug=slug)

@login_required
def favourite_post_list(request):
    user = request.user
    favourite_posts = user.favourite.all()
    context = {
        'favourite_posts': favourite_posts,
    }
    return render(request, 'main/favourite_posts.html', context)

