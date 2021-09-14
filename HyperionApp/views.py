from django.shortcuts import render
from django.http import HttpResponse
from .forms import signup_form
from .forms import login_form
from django import forms
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method == 'GET':
        return render(request, 'signup.html')

    elif request.method == 'POST':

        return HttpResponse(request)
        signup_instance = signup_form(request.POST)


        if not signup_instance.is_valid():
            return render(request, 'signup.html', context={'errors': signup_instance.errors.values()})

        else:
            title = signup_instance.cleaned_data['title']
            first_name = signup_instance.cleaned_data['first_name']
            last_name = signup_instance.cleaned_data['last_name']

            dob_concatenated = signup_instance.cleaned_data['dob_day'] + "/" + signup_instance.cleaned_data['dob_month'] + "/" + signup_instance.cleaned_data['dob_year']

            encrypted_password = make_password(password)

            add_db = User(title=title, first_name=first_name, last_name=last_name, dob=dob_concatenated, email=email, password=encrypted_password)
            add_db.save()

            return HttpResponse("thank you")


def login(request):
    if request.method=='GET':
        return render(request, 'login.html')

    elif request.method=='POST':
        # Create an instance of your login_form
        login_instance = login_form(request.POST)

        # Input validation (it triggers the conditions written in forms.py)
        if not login_instance.is_valid():
            return render(request, 'login.html', context={'errors': login_instance.errors.values()})

        return render(request, 'dashboard.html')
