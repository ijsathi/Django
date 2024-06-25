from django import forms
from .models import Comment
from django.contrib.auth.models import User
from django.views.generic import UpdateView
from django.contrib.auth.forms import UserChangeForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']

class CustomUserChangeForm(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

class UserProfileView(UpdateView):
    model = User
    fields = ('first_name', 'last_name', 'email')
    template_name = 'profile.html' 
    
    # ... rest of the code remains the same

