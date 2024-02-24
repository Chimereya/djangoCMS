from django.urls import path
from . import views



app_name = 'user'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('login/', views.LoginCustomView.as_view(), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('<username>/', views.profile, name='profile'),
    path('<username>/edit_profile/', views.edit_profile, name='edit_profile'),
    path('follow', views.follow, name='follow'),
]