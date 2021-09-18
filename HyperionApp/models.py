from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class User(AbstractUser):
    title = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=12)
    email = models.CharField(max_length=254, unique=True)
    password = models.CharField(max_length=50)

    REQUIRED_FIELDS=[]
    # This forces Django to use the email as the username. The username is
    # used as part of the authentication checks performed by
    # `authenticate()` function
    USERNAME_FIELD='email'
