from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.CreatepostView.as_view(), name='create'),
    path('posts/<str:username>/', views.PostView.as_view(), name='user_post_list'),
    path('posts/', views.PostListView.as_view(), name='posts'),
    path('<slug:slug>/', views.PostDetailView.as_view(), name='detail'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'), 
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'), 
    path('<str:username>/blog/', views.user_blog_page, name='user_page'),
    path('post/<slug:slug>/like/', views.like_post, name='like_post'),
    path('post/<slug:slug>/bookmark/', views.bookmark_post, name='bookmark_post'),
    path('bookmarks/', views.bookmark_list, name='bookmarks'),
    ]