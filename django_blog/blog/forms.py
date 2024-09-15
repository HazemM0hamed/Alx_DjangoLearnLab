from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile, Post, Comment, Tag
from taggit.forms import TagField, TagWidget

class PostForm(forms.ModelForm):
    tags = forms.CharField(widgets=TagWidget(), required=False)
    
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']