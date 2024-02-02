from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model
from .models import CustomUser

class SignUpForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name','username', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'password')


class UpdateUserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
    profile_pic = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control-file'}))

    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']