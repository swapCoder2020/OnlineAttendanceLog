from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def registrationPage(request):
    return render(request, 'registration.html')
    # return HttpResponse("Hello test")