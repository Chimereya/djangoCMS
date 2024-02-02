from django.forms import ModelForm
from .models import Profile
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth import get_user_model


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