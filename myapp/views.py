from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='Login')
def index(request):
    return render(request, "myapp/index.html")

def SignUp(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('pass')
        confirm_password = request.POST.get('cpass')
        # print(username, email, password, confirm_password)
        if password != confirm_password:
            messages.error(request, "Passwords are not matched")
            # return redirect('SignUp')
        else:
            my_user = User.objects.create_user(username, email, password)
            my_user.save()
        return redirect("Login")
    return render(request, "myapp/register-page.html")


def Login(request):
    try: 
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('Index')
        else:
            # messages.error(request, "Invalid passowrd")
            return render(request, "myapp/login-page.html")
    except Exception as e:
        messages.error(request, "Got an unexpected error.")

def Logout(request):
    logout(request)
    return redirect("/")

# def Login(request):
#     username  = request.POST.get('username')
#     password = request.POST.get('password')
#     # print(username, email, password)
#     user = authenticate(request, username=username, password=password)
#     # print(user)
#     if user is not None:
#         login(request, user)
#         return redirect('Index')
#     else:
#         messages.error(request, "Incorrect Password")
#     return render(request, "myapp/login-page.html")