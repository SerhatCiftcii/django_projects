from django.shortcuts import render
from django.template.context_processors import request
from django.contrib.admin import register
from django.contrib.auth import logout

# Create your views here.
def login_request(request):
    return render(request, "account/login.html")
def register_request(request):
    return render(request,"account/register.html")

def change_password(request):
    return render(request,"account/change_password.html")

def logout_request(request):
    return render(request,"account/change_password.html")
