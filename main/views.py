from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required



class HomeView(ListView):
    model = Post
    template_name = 'main/home.html'
    
    
class PostDetailView(DetailView):
    model = Post
    template_name = 'main/detail.html'
    context_object_name = 'post'
    slug_url_kwarg = 'slug'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.view_count += 1  # Increment view count
        obj.save()
        return obj

    
    
class PostView(ListView):
    model = Post
    template_name = 'main/posts.html'
    context_object_name = 'blog_list'
    
    
class CreatepostView(CreateView):
    model = Post
    template_name = 'main/create.html'
    context_object_name = 'blog_list'
    fields = ['title', 'tags', 'content', 'image', 'image_credit', 'author', 'status']
    success_url = reverse_lazy('blog:posts')
    
    
class EditView(UpdateView):
    model = Post
    template_name = 'main/edit.html'
    fields = ['title', 'tags', 'content', 'image', 'image_credit', 'author', 'status']
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')
    

class Delete(DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')
    template_name = 'main/delete.html'



def like_post(request, pk):
    post = Post.objects.get(id=pk)
    user = request.user
    if request.user in post.likes.all():
        post.likes.remove(user)
    else:
        post.likes.add(user)
    return redirect('blog:detail', slug=post.slug)




