from django.db import models

class Users(models.Model):
    first_name = models.CharField(max_length=20, blank=False)
    middle_name = models.CharField(max_length=20, blank=False)
    last_name = models.CharField(max_length=20, blank=True)
    contact = models.IntegerField(blank=False)
    address = models.CharField(max_length=300, blank=False)
    username = models.CharField(max_length=20, blank=False, unique=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=30, blank=False)

    def __str__(self):
        return "{} {} {}".format(Users.first_name, Users.last_name, Users.email)