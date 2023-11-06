from typing import Any
from django import forms
from django.contrib.auth.models import User
from .models import Profile

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','email']
    
    def clean_password2(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']
        if password!=password2:
            raise forms.ValidationError('Password don\'t match')
        return password2
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already resitered")
        return email
        
class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','email']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        qs = User.objects.exclude(id=self.instance.id).filter(email=email)
        if qs.exists():
            raise forms.ValidationError("Email is already resitered")
        return email

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']