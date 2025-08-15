from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def index_page(request):
    return render(request, 'index.html')

def child_page(request):
    return render(request, 'child.html')

def teen_page(request):
    return render(request, 'teen.html')

def adult_page(request):
    return render(request, 'adult.html')

def features_page(request):
    return render(request, 'features.html')

def security_page(request):
    return render(request, 'security.html')

def teen_challenge_page(request):
    return render(request, 'teen-challenge.html')

def adult_challenge_page(request):
    return render(request, 'adult-challenge.html')

def child_challenge_page(request):
    return render(request, 'child-challenge.html')

def teen_progress_page(request):
    return render(request, 'teen-progress.html')

def adult_progress_page(request):
    return render(request, 'adult-progress.html')

def child_progress_page(request):
    return render(request, 'child-progress.html')

def child_rewards_page(request):
    return render(request, 'child-rewards.html')
