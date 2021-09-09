from django.db import models

# Create your models here.
class User(models.Model):
    title = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=100)
    dob = models.CharField(max_length=12)
    email = models.CharField(max_length=254)
    password = models.CharField(max_length=50)
