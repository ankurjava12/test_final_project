from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, 'basicapp/html/index.html')


def about(request):
    return render(request, 'basicapp/html/about.html')

def contact(request):
    return render(request, 'basicapp/html/contact.html')


# Feedback--
def feedback(request):
    
    return render(request, 'basicapp/html/feedback.html')