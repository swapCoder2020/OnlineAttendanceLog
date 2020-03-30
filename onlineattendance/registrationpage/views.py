from django.shortcuts import render
from django.http import HttpResponse
from .models import Users
from django.contrib.auth.models import User

def registrationPage(request):
    if request.method == "POST":
        try:
            usr = Users()
            usr.first_name = request.POST['first_name']
            usr.middle_name = request.POST['middle_name']
            usr.last_name = request.POST['last_name']
            usr.contact = request.POST['contact']
            usr.address = request.POST['address']
            usr.username = request.POST['username']
            usr.email = request.POST['email']
            usr.password = request.POST['password']
            auth_usr = User(**{'username': request.POST['username'],
                               'email': request.POST['email'],
                               'first_name': request.POST['first_name'],
                               'last_name': request.POST['last_name']})
            auth_usr.set_password(request.POST['password'])
            auth_usr.save()
            usr.save()
        except Exception as ex:
            context = {'response': str(ex)}
            return render(request, 'registration.html', context)
    return render(request, 'registration.html')