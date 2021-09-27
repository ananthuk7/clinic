from django.shortcuts import render, redirect
from owner import forms
from owner.models import Doctors, Appoinment


# Create your views here.
def dashboard(request):
    appoiment = Appoinment.objects.all()
    context = {'appoinments': appoiment}
    return render(request, 'dashboard.html', context)


def add_doctor(request):
    form = forms.AddDoctorForm()
    if request.method == 'POST':
        form = forms.AddDoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'adddoctors.html', {'form': form})
    return render(request, 'adddoctors.html', {'form': form})


def change_doctor(request, id):
    doctor = Doctors.objects.get(id=id)
    form = forms.DoctorChange(instance=doctor)
    if request.method == 'POST':
        form = forms.AddDoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'editdoctors.html', {'form': form})
    return render(request, 'editdoctors.html', {'form': form})


def view_doctors(request):
    doctor = Doctors.objects.all()
    return render(request, 'viewdoctors.html', {'doctors': doctor})


def delete_doctor(request, id):
    doctor = Doctors.objects.get(id=id)
    doctor.delete()
    return redirect('viewdoctor')


def details_doctor(request, id):
    doctor = Doctors.objects.get(id=id)
    return render(request, 'detaildoctor.html', {'doctors': doctor})


def send_message(request, id):
    users = Appoinment.objects.get(id=id)
    form = forms.MessageForm(initial={'users': users})
    if request.method == "POST":
        form = forms.MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
        else:
            return render(request, 'message.html', {'form': form})
    return render(request, 'message.html', {'form': form})
