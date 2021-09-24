from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import signup_form
from .forms import login_form
from django import forms
from .models import User
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth import authenticate, login, logout
import random

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):

    if request.user.is_authenticated:
        return redirect('HyperionApp:dashboard')

    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':

        signup_instance = signup_form(request.POST)

        if not signup_instance.is_valid():
            return render(request, 'signup.html', context={ 'form': signup_instance })

        else:
            # Prepare user's inputs to be sent to the db
            title = signup_instance.cleaned_data['title']
            first_name = signup_instance.cleaned_data['first_name']
            last_name = signup_instance.cleaned_data['last_name']

            dob_concatenated = signup_instance.cleaned_data['dob_day'] + "/" + signup_instance.cleaned_data['dob_month'] + "/" + signup_instance.cleaned_data['dob_year']

            email = signup_instance.cleaned_data['email']
            password = signup_instance.cleaned_data['password']

            encrypted_password = make_password(password)

            # Generate random credit score
            credit_score = random.randint(300, 999)

            # Send credit score and inputs to db
            add_db = User(title=title, first_name=first_name, last_name=last_name, dob=dob_concatenated, email=email, password=encrypted_password, credit_score=credit_score)
            add_db.save()

            return redirect('HyperionApp:login')


def signin(request):

    if request.user.is_authenticated:
        return redirect('HyperionApp:dashboard')

    if request.method=='GET':
        return render(request, 'login.html')

    elif request.method=='POST':
        # Create an instance of your login_form
        login_instance = login_form(request.POST)

        # Input validation (it triggers the conditions written in forms.py)
        if not login_instance.is_valid():
            return render(request, 'login.html', context={'errors': login_instance.errors.values()})

        # Django forces you to use `is_valid` before cleaning data. There is no
        # `cleaned_data` before `is_valid`
        username = login_instance.cleaned_data['email']
        password = login_instance.cleaned_data['password']

        # Authentication checks. Django provides this by default (checks if
        # username exists, if password is correct)
        user = authenticate(request, username=username, password=password)

        # Handle authentication error
        if user is None:
            errors = ['Username and password do not match our records']
            return render(request, 'login.html', context={'errors': errors })

        # Create session
        login(request, user)

        return redirect('HyperionApp:dashboard')

def dashboard(request):
    # Limit access to dashboard if users are not logged-in
    if request.user.is_authenticated:
        return render(request, 'dashboard.html')

    else:
        return redirect('HyperionApp:login')

def signout(request):
    logout(request)
    return redirect('HyperionApp:index')
