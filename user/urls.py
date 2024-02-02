from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('<username>/', views.profile, name='profile'),
    path('<username>/edit_profile/', views.edit_profile, name='edit_profile'),

]