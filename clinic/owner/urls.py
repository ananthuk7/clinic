from django.urls import path
from owner import views

urlpatterns = [
    path('clinic/dashboard/', views.dashboard, name="dashboard"),
    path('clinic/add', views.add_doctor, name="adddoctor"),
    path('clinic/change/<int:id>', views.change_doctor, name="editdoctor"),
    path('clinic/doctors/list', views.view_doctors, name="viewdoctor"),
    path('clinic/doctor/change/remove/<int:id>', views.delete_doctor, name="deletedoctor"),
    path('clinic/doctor/message/<int:id>',views.send_message,name='message')
]
