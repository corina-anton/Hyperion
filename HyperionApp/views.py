from django.shortcuts import render
from django.http import HttpResponse
from .forms import signup_form
from .forms import login_form
from .models import User
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def index(request):
    return render(request, 'index.html')

def signup(request):
    if request.method=='GET':
        return render(request, 'signup.html')

    elif request.method=='POST':

        # Retrieve the data sent by the use through HTTP:
        signup_instance = signup_form(request.POST)

        # Input validation:
        if not signup_instance.is_valid():
            return HttpResponse("error")

        # Part of input validation: Verify whether the email already exists in the database
        email = signup_instance.cleaned_data['email']
        db_email = User.objects.all().filter(email=email)

        if len(db_email) > 0:
            return HttpResponse("There is another account created with this email")

        # Part of input validation: Verify if confirm_password and password inputs are identical
        password = signup_instance.cleaned_data['password']
        confirm_password = signup_instance.cleaned_data['confirm_password']

        if password != confirm_password:
            return HttpResponse("error")

        # Send to db
        else:
            title = signup_instance.cleaned_data['title']
            first_name = signup_instance.cleaned_data['first_name']
            last_name = signup_instance.cleaned_data['last_name']

            # Concatenate dob
            dob_concatenated = signup_instance.cleaned_data['dob_day'] + "/" + signup_instance.cleaned_data['dob_month'] + "/" + signup_instance.cleaned_data['dob_year']

            email = signup_instance.cleaned_data['email']

            # Encrypt password
            password = make_password(signup_instance.cleaned_data['password'])

            # Add to db
            add_db = User(title=title, first_name=first_name, last_name=last_name, dob=dob_concatenated, email=email, password=password)
            add_db.save()

            return HttpResponse("thank you")


def login(request):
    if request.method=='GET':
        return render(request, 'login.html')

    elif request.method=='POST':
        # Create an instance of your login_form
        login_instance = login_form(request.POST)

        if not login_instance.is_valid():
            return HttpResponse("error")
        # Extract the needed data using the `cleaned_data[""]`
        email = login_instance.cleaned_data['email']
        password = login_instance.cleaned_data['password']

        # Extract the row in the database whose email = request email.
        user = User.objects.all().filter(email=email)

        # Verify that the data (usernam/email) is the same with the data in the db
        if len(user) == 0:
            return HttpResponse("username or password does not match our records")

        if not check_password(password, user[0].password):
            return HttpResponse("username or password does not match our records")

        return render(request, 'dashboard.html')
