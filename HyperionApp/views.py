from django.shortcuts import render
from django.http import HttpResponse
from .forms import signup_form
from .models import User

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html')

    elif request.method=='POST':

        # Input validation
        # Verify that the confirm_password form field is identical
        signup_instance = signup_form(request.POST)

        if not signup_instance.is_valid or signup_instance.cleaned_data['password'] != signup_instance.cleaned_data['confirm_password']:
            return HttpResponse("error")

        # Send to db
        else:
            title=signup_instance.cleaned_data['title']
            first_name=signup_instance.cleaned_data['first_name']
            last_name=signup_instance.cleaned_data['last_name']

            # Concatenate dob
            dob_concatenated = signup_instance.cleaned_data['dob_day'] + "/" + signup_instance.cleaned_data['dob_month'] + "/" + signup_instance.cleaned_data['dob_year']

            email=signup_instance.cleaned_data['email']
            password=signup_instance.cleaned_data['password']

            add_db = Users(title=title, first_name=first_name, last_name=last_name, dob=dob_concatenated, email=email, password=password)
            add_db.save()

            return HttpResponse("thank you")


def login(request):
    return render(request, 'login.html')
