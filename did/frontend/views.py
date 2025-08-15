from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def index_page(request):
    return render(request, 'index.html')
