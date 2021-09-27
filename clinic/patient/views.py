from django.shortcuts import render, redirect
from owner.models import Doctors, Appoinment, Notification
from patient import forms
from django.contrib.auth import authenticate, login, logout
from patient.decorators import user_login_required


# Create your views here.
def index(request):
    doctor = Doctors.objects.all()
    context = {'doctors': doctor}
    return render(request, 'base.html', context)


@user_login_required
def appoinment(request, id, *args, **kwargs):
    appoint = Doctors.objects.get(id=id)
    form = forms.AppoinmentForm(initial={'doctors': appoint})
    if request.method == 'POST':
        form = forms.AppoinmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            appointment.user = request.user
            appointment.save()
            return redirect('home')
        else:
            return render(request, 'makeappoinment.html', {'form': form})
    return render(request, 'makeappoinment.html', {'form': form})


def sign_in(request):
    form = forms.UserSigninForm()
    if request.method == 'POST':
        form = forms.UserSigninForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('home')
            else:
                return render(request, 'signin.html', {'form': form})
        else:
            return render(request, 'signin.html', {'form': form})
    return render(request, 'signin.html', {'form': form})


def sign_up(request):
    form = forms.UserRegistrationForm()
    if request.method == 'POST':
        form = forms.UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
        else:
            return render(request, 'signup.html', {'form': form})
    return render(request, 'signup.html', {'form': form})


@user_login_required
def sign_out(request, *args, **kwargs):
    logout(request)
    return redirect('home')


@user_login_required
def notification(request, *args, **kwargs):
    notifications = Notification.objects.filter(users__user=request.user)
    context = {'notifications': notifications}
    return render(request, 'notification.html', context)


@user_login_required
def startpage(request, *args, **kwargs):
    notifications = Notification.objects.filter(users__user=request.user)
    total_notification=notifications.count()
    context = {'total_notifications': total_notification}
    return render(request, 'index.html', context)
