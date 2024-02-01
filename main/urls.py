from . import views
from django.urls import path

app_name = 'main'

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('create/', views.CreatepostView.as_view(), name='create'),
    path('posts/', views.PostView.as_view(), name='posts'),
    path('<slug:slug>/', views.detail_view, name='detail'),
    path('edit/<int:pk>/', views.EditView.as_view(), name='edit'), 
    path('delete/<int:pk>/', views.Delete.as_view(), name='delete'), 
]