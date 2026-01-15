from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, UserCreationForm
from django.template.context_processors import request

from account.forms import LoginUserForm, NewUserForm


# Create your views here.
def login_request(request):
    
    if request.user.is_authenticated: # bu sessionid  alıyor login tekrar yapmamızı sağlıyor
        return redirect("products")
    if request.method=="POST":
        # form = AuthenticationForm(request, data=request.POST)
        form = LoginUserForm(request, data=request.POST)
        if form.is_valid():
            username= form.cleaned_data.get("username")
            password= form.cleaned_data.get("password")
            user= authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request,user)
                return redirect("products")
            else:
                return render(request, "account/login.html",{
                    "form":form
                })
        else:
             return render(request, "account/login.html",{
                    "form":form
                })
    else:
        form =LoginUserForm()
        return render(request, "account/login.html",{
            "form":form
        })
        
            
        
        
        
        
        # alltaki işlem form yapısı geldikten sonra iptal oldu
    #     username=request.POST["username"]
    #     password=request.POST["password"]
        
    #     user = authenticate(request, username=username,password=password)
    #     if user is not None:
    #         login(request,user)
    #         nextUrl= request.GET.get("next", None) # yetki olmayan yerlerde login olmadıysak ve sonra login olduysak o anki login olmadığımız yuetkilenmediğimiz yere gideriz.
    #         if nextUrl is None:
    #             messages.success(request, "Login başarılı")
    #             return redirect("products")
    #         else:
    #             return redirect(nextUrl)
    #     else:
    #         messages.error(request,"username yada parola yanlış")
    #         return render(request, "account/login.html")
    
        
    # else:
    #     return render(request, "account/login.html")
    

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST) # BUDAREGİSTER İÇİN DİREKT HAZIR FORM bunuda autform gibi genişletebilirz miraz alarak
        
        if form.is_valid():
            form.save()
            username = form.cleaned_data[ "username"]
            password = form.cleaned_data[ "password1"]
            user = authenticate(username=username , password=password)
            login(request, user)
            return redirect("products")
        else:
            return render (request,"account/register.html",{
                "form":form
            })
    else:
        form=NewUserForm()
    
    return render(request,"account/register.html",{
        "form":form
    })
        
    
        
        
        
        
        #eski kod allta 
    #     username= request.POST["username"]
    #     email= request.POST["email"]
    #     password= request.POST["password"]
    #     repassword= request.POST["repassword"]
        
    #     if password == repassword:
    #         if User.objects.filter(username=username).exists(): #exits tru yada false dönderirir bu kullancıya ait başka kullanıc varmı diye sorar
    #             return   render(request, "account/register.html",{
    #             "error":"Username kullanılıyor."
    #         })
    #         else:
    #             if User.objects.filter(email=email).exists():
    #                 return render(request, "account/register.html",{
    #                     "error":"bu email kullanılıyor."
    #         })
    #             else:
    #                 user=User.objects.create_user(username=username, email=email, password=password)
    #                 user.save()
    #                 return redirect("login")
                    
    #     else:
    #         return render(request, "account/register.html",{
    #             "error":"Parola eşleşmiyor"
    #         })
        
    # else:
    #     return render(request, "account/register.html")

def change_password(request):
    if request.method=="POST":
            form= PasswordChangeForm(request.user, request.POST) # login olan kullanıcı bu işelmi yapmasıiçin bu layoutdanda is atuhentaıd demek lazım headerdan yani
            if form.is_valid():
                user= form.save()
                update_session_auth_hash(request, user)
                messages.success(request,"Parola değiştirlidi")
                return redirect("change_password")
            else:
                return render(request,"account/change_password.html",{
                    "form":form
                })
   
    form=PasswordChangeForm(request.user)
    return render(request,"account/change_password.html",{
                    "form":form
                })
         
def logout_request(request):
    logout(request)
    messages.error(request,"Çıkış Başarılı")
    return redirect("products")