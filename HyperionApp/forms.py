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

    # Verify if there already is an account that uses the same email;
    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")

        user = User.objects.all().filter(email=email)

        if len(user) > 0:
            raise forms.ValidationError("There already is an account that uses this email")
        else:
            return email

    # Verify if the password and confirm password fields match;
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")
        else:
            return cleaned_data

        # The 'def clean_password' method does cleaning specific to that
        # particular attribute.
        # The 'def clean()' method performs validation that requires access
        # to multiple form fields.
        # Here you must use `def clean(self)` and not `def clean_password`.
        # This is because the order of 'cleaning' matters.
        # If you use `def clean_password`, django will only clean the
        # 'password' input BUT you need the 'confirm_password' as well which
        # not yet cleaned.

class login_form(forms.Form):
    email = forms.EmailField(label='Email', max_length=254)
    password = forms.CharField(max_length=254)

    # Verify that the email exists in the database;
    # def clean_email(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data.get("email")
    #
    #     user = User.objects.all().filter(email=email)
    #
    #     if len(user) == 0:
    #         raise forms.ValidationError("Username and password do not match our records")
    #     else:
    #         return email
    #
    # # Verify if the password matches the one in the db;
    # def clean_password(self):
    #     cleaned_data = super().clean()
    #     email = cleaned_data.get("email")
    #     password = cleaned_data.get("password")
    #
    #     user = User.objects.all().filter(email=email)
    #
    #     if not check_password(password, user[0].password):
    #         raise forms.ValidationError("Username and password do not match our records")
    #     else:
    #         return password
