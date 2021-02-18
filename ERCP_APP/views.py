from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request,'index.html')

def login_user(request):
    return render(request, 'ercp_admin/login.html')

def logout_user(request):
    logout(request)
    return redirect(login_user)


@login_required(login_url='/login/')
def option(request):
    return render(request, 'ercp_admin/option.html')

def authenticate_user(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            return redirect(option)
        else:
            return render(request, "ercp_admin/login.html", {"error": "Invalid Credentials"})

    return render(request, "ercp_admin/login.html")