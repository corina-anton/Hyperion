# Hyperion - Mock credit score app

## Description

## Features

## What I've learned

- How to create a basic layout structure using Bootstrap CSS framework;
- How to customise the layout using HTML & CSS (https://www.coursera.org/learn/html-css-javascript-for-web-developers/);
- How to use forms and process the data on backend for log-in and sign-in features;
- How to set up a database using Django models and migrations, as well as entering and extracting data from the database as needed;
- Input validation;
- Password encryption;
- How to perform authentication and authorization checks, both manually and using Django built-in functions (`authenticate()`, `login()`, `logout()`)
- How to apply the KISS principle in coding (see input validation in `forms.py` vs. Django `authenticate()`)

## Key takeaways

- To access data from HTTP params, you need to use `request.cleaned_data['<param>']`;

- The link between html inputs and forms is the `name="[e.g. email]"` attribute nested inside the input tag. You need to use the same attribute when you create the form;

- Why do you need to create a form instance in view? (eg: `login_instance = login_form(request.POST)`)
  The HTTP request posts back raw data. For example, the login page of Hyperion sends back `csrfmiddlewaretokenemailpassword`. Next, the class `login_form(request.POST)` processes the raw data, validates it, and creates various objects (see Django [source code](https://github.com/django/django/blob/main/django/forms/forms.py)). Some of these objects are:
      - `errors`
      - `is_valid`
      - `cleaned_data`: It generates a cleaned list where the keys are the parameter names in your form (e.g. email, password) and the value is users' input. In order to use these parameters, you must access them using: `login_instance.cleaned_data['email']`

  **NOTE 1:**  Forms only get a `cleaned_data` attribute when `is_valid()` has been called.
  **NOTE 2:** The `login_instance` is just holds these objects in order for them to be used further.

## Logic workflow

**Basic sign-up page:**
![](https://i.imgur.com/lBoipqf.png)

    1.  The user fills up the form in the browser. The data is then sent to the server (HTTP, POST method). In order to access this data, you must create an instance of the form (see above);
    2. Input validation:
       - Verify whether the forms conditions have been met;
       - Verify whether the email address already exists. If yes, send error message.
       - Verify whether the password input matches the confirm_password input. If no, send error message. If yes, continue to encryption.
    3. Password encryption;
    4. Save users' inputs into the database;
    5. Display success message;

**Basic sign-in page:**
![](https://imgur.com/a/RB7QPuq)

    1. The user fills up the login form in the browser. The data is then sent to the server through the HTTP request using the POST method. In order to access the data, you must create an instance of the form;
    2. Input validation: checks if the general conditions set in `forms.py` have been met;
    3. Authentication checks:
       - check if the email exists in the database; if no, raise custom error;
       - check if the password matches the one stored in the database; if no, raise custom error;
    4. Log the user in. This creates a user session;
