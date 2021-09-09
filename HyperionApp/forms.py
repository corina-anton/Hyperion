from django import forms

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
