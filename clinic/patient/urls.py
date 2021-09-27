from django.urls import path
from patient import views

urlpatterns = [
    path('', views.index, name="home"),
    path('makeappoinment/<int:id>', views.appoinment, name='appoinment'),
    path('accounts/signin', views.sign_in, name='signin'),
    path('accounts/signup', views.sign_up, name='signup'),
    path('accounts/signout', views.sign_out, name='signout'),
    path('notification', views.notification, name="msg"),
    path('home/hide', views.startpage,name="startpage")
]
