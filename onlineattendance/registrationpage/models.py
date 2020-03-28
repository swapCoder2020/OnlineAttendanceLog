from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    middle_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=True)
    contact = models.CharField(max_length=10, blank=False)
    address = models.CharField(max_length=300, blank=False)
    username = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)