from django.forms import ModelForm
from django import forms
from owner.models import Doctors, Appoinment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class AppoinmentForm(ModelForm):
    class Meta:
        model = Appoinment
        fields = ['doctors', 'phone', 'address']
        widgets = {
            'doctors': forms.Select(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'email', 'username', 'password1', 'password2']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }


class UserSigninForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
