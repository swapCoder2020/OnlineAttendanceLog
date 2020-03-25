from django.shortcuts import render, redirect

# Create your views here.
def mainPage(request):
    if request.method == 'GET':
        try:
            if request.GET['Register']:
                return redirect('registrationPage')
        except:
            pass
        try:
            if request.GET['Login']:
                return redirect('loginPage')
        except:
            pass
        return render(request, 'main.html')