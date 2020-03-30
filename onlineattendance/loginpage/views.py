from django.shortcuts import render, redirect
from django.contrib import auth

def loginPage(request):
    if request.method == 'POST':
        user_ok = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user_ok is not None:
            auth.login(request, user_ok)
        return redirect('/')
    return render(request, 'login.html')

def logoutPage(request):
    auth.logout(request)
    return redirect('/')