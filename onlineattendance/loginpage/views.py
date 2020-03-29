from django.shortcuts import render, redirect

# Create your views here.
def loginPage(request):
    if request.method == 'POST':

        return redirect('/')
    return render(request, 'login.html')