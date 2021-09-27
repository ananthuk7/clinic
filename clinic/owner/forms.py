from django.forms import ModelForm
from django import forms
from owner.models import Doctors, Notification


class AddDoctorForm(ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'specialized': forms.TextInput(attrs={'class': 'form-control'}),
            'sheduletime': forms.TextInput(attrs={'class': 'form-control'})

        }


class DoctorChange(ModelForm):
    class Meta:
        model = Doctors
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'specialized': forms.TextInput(attrs={'class': 'form-control'}),
            'sheduletime': forms.TextInput(attrs={'class': 'form-control'})

        }


class MessageForm(ModelForm):
    class Meta:
        model = Notification
        fields = '__all__'
        widgets = {
            'users': forms.Select(attrs={'class': 'form-control'}),
            'message': forms.Textarea(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'reporting_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'})
        }
