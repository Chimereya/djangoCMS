from django import forms
from .models import Post
from django.contrib.auth.models import User


class CreateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"