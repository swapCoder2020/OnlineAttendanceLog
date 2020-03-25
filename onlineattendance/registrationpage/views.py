from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def registrationPage(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'registration.html')