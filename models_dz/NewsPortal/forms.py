from django import forms
from .models import Post
from django.forms import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['author', 'postCategory', 'title', 'text']
