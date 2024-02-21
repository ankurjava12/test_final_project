# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('feedback/',views.feedback, name="feedback"),
    path('contact/',views.contact, name="contact"),
    path('login/',views.login, name="login"),
]