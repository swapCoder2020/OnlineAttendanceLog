from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import Users

def registrationPage(request):
    if request.method == "POST":
        credentialDict = dict(request.POST)
        del credentialDict['csrfmiddlewaretoken']
        del credentialDict['Confirm Password']
        del credentialDict['submit']

        try:
            usr = Users(**credentialDict)
            usr.save()
        except Exception as ex:
            context = {'response': str(ex)}
            return render(request, 'registration.html', context)

    return render(request, 'registration.html')