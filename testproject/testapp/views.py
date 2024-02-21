from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse("<h1>This is a home page.</h1>")

def about(request):
    return HttpResponse("<h1>This is a about us page.</h1>") 

def feedback(request):
    return HttpResponse("<h1>This is a feddback page.</h1>") 

def contact(request):
    return HttpResponse("<h1>This is a contact us page.</h1>") 

def login(request):
    return HttpResponse("<h1>This is a login page.</h1>.") 