from django import forms
from .models import User
from django.contrib.auth.hashers import make_password, check_password

class signup_form(forms.Form):
    title = forms.CharField(max_length=150)
    first_name = forms.CharField(label='Last name(s)', max_length=150)
    last_name = forms.CharField(label='First Name', max_length=100)
    dob_day = forms.CharField(label='Dob_day', max_length=2)
    dob_month = forms.CharField(label='Dob_month', max_length=2)
    dob_year = forms.CharField(label='Dob_year', max_length=4)
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(max_length=254)
    confirm_password = forms.CharField(max_length=254)

class login_form(forms.Form):
    email= forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(max_length=254)

    # Verify that the email exists in the database;
    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        user = User.objects.all().filter(email=email)

        if len(user) == 0:
            raise forms.ValidationError("Username and password do not match our records")
        else:
            return email

    # Verify if the password matches the one in the db;
    def clean_password(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        user = User.objects.all().filter(email=email)

        if not check_password(password, user[0].password):
            raise forms.ValidationError("Username and password do not match our records")
        else:
            return password
