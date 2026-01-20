from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.contrib.admin import register
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.forms import LoginForm
# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            if User.objects.filter(email=email).exists(): # true gelirse veri tabanına  kayıt vardır  bi içeri alırız mailvarsada giriş olur yoksa boş formuj çıakrıız yada else  yzarak hata mesajıyla birlikte dönerderiiz
                username= User.objects.get(email=email).username
                user = authenticate(username=username, password=password)
            else:
                 return render(request, "account/login.html",{
                    "form":form
                })
            
            if user is not None:
                login(request, user)
                return redirect("home_page")
            else:
                form.add_error(None, "email yada parola yanlıştır")
                return render(request, "account/login.html",{
                    "form":form
                })
        else:
            form.add_error(None, "email ile kayıtlı bi kuallnıcı yoktur")
            return render(request, "account/login.html",{
                    "form":form
                })

    form = LoginForm()
    return render(request, "account/login.html",{
        "form":form
    })
def register_request(request):
    return render(request,"account/register.html")

def change_password(request):
    return render(request,"account/change_password.html")

def logout_request(request):
    return render(request,"account/change_password.html")
