from django.shortcuts import render
from django.http import HttpResponse
from .models import PropertyOwner, User

def user_signup(request):
    return render(request, 'signup.html')

def user_login(request):
    return render(request, 'login.html')

def owner_signup(request):
    return render(request, 'owner_signup.html')
def home(request):
    return HttpResponse("Welcome to the Inventory Management System!")