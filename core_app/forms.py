from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from . import models

class SignupForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password1',
            'password2',
        ]
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Username',
        'class': 'px-4 py-2 text-lg w-full rounded-xl'
    }))
    
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Email',
        'class': 'px-4 py-2 text-lg w-full rounded-xl'
    }))
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'px-4 py-2 text-lg w-full rounded-xl'
    }))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Password',
        'class': 'px-4 py-2 text-lg w-full rounded-xl'
    }))
    

class LoginForm(AuthenticationForm):
    
    class Meta:
        model = User
        fields = ['username', 'password']
        
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Your Username',
        'class': 'px-6 py-3 rounded-xl bg-white w-3/4',
    }))
    
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Your Password',
        'class': 'px-6 py-3 rounded-xl bg-white w-3/4',
    }))
    
class ProfileForm(forms.ModelForm):
    
    class Meta:
        model = models.UserProfile
        fields = ['avatar', 'biography']
        
    avatar = forms.ImageField()
    
    biography = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Tell who you are . . . ',
        'class': 'px-6 py-3 text-xl rounded-xl bg-white w-3/4',
    }))