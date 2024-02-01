from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy


class HomeView(ListView):
    model = Post
    template_name = 'main/home.html'
    
    
def detail_view(request, slug):
    post = get_object_or_404(Post, slug=slug)

    return render(request, 'main/detail.html', {'post': post})
    
    
class PostView(ListView):
    model = Post
    template_name = 'main/posts.html'
    context_object_name = 'blog_list'
    
    
class CreatepostView(CreateView):
    model = Post
    template_name = 'main/create.html'
    context_object_name = 'blog_list'
    fields = '__all__'
    success_url = reverse_lazy('blog:posts')
    
    
class EditView(UpdateView):
    model = Post
    template_name = 'main/edit.html'
    fields = '__all__'
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')
    

class Delete(DeleteView):
    model = Post
    pk_url_kwarg = 'pk'
    success_url = reverse_lazy('blog:posts')
    template_name = 'main/edit.html'



