from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import PropertyOwner
from django.contrib.auth.models import User 
from django.contrib import messages
from django.contrib.auth import authenticate, login

def user_signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if not username or not email or not password:
            return render(request, 'signup.html', {'error_message': 'All fields are required!'})
        # Create the user
        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            # return HttpResponse("User created successfully!")
            user.is_active = False  # Set the user as inactive
            user.save()  # Save the changes to the user object
            return render(request, 'activation.html')
        except Exception as e:
            return render(request, 'signup.html', {'error_message': f"Error: {e}"})

        messages.success(request, 'Signup successful! Please wait for admin approval.')
        return redirect('activation')  # Redirect to activation page

    return render(request, 'signup.html')

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('home')  # Redirect to home after login
            else:
                return redirect('activation')  # Redirect inactive users to activation page
        else:
            messages.error(request, 'Invalid username or password.')

    return render(request, 'login.html')

def activation(request):  # New activation function
    return render(request, 'activation.html')

def owner_signup(request):
    return render(request, 'owner_signup.html')

def home(request):
    return HttpResponse("Welcome to the Inventory Management System!")