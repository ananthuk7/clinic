from django.db import models


# Create your models here.

class Doctors(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(max_length=100)
    options = (
        ('male', 'male'),
        ('female', 'female'),
        ('others', 'others')
    )
    gender = models.CharField(max_length=10, choices=options,default='male')
    specialized = models.CharField(max_length=100)
    sheduletime = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appoinment(models.Model):
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    user = models.CharField(max_length=50)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=120)

    def __str__(self):
        return self.user


class Notification(models.Model):
    users = models.ForeignKey(Appoinment, on_delete=models.CASCADE)
    message = models.CharField(max_length=120)
    date = models.DateField(null=True)
    reporting_time = models.TimeField(null=True)

