from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Extend, StudentExtend

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']

class UserExtensionForm(forms.ModelForm):
    class Meta:
        model = Extend
        fields = ['tag']

class StudentExtensionForm(forms.ModelForm):
    class Meta:
        model = StudentExtend
        fields = ['section']
