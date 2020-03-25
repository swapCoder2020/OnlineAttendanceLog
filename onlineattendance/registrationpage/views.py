from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Users

def registrationPage(request):
    if request.method == "POST":
        temp = Users(**{'first_name':'chinmay', 'middle_name':'rajan', 'last_name':'gharat'
                        ,'contact':7507511126, 'address':'avasasda asdad', 'username':'chinu', 'email':'c@c.com', 'password':'qwerty1234'})
        temp.save()
    return render(request, 'registration.html')