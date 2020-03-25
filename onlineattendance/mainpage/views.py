from django.shortcuts import render

# Create your views here.
def mainPage(request):
    if request.method == 'GET':
        try:
            if request.GET['Register']:
                return render(request, 'registration.html')
        except:
            pass
        try:
            if request.GET['Login']:
                return render(request, 'login.html')
        except:
            pass
        return render(request, 'main.html')