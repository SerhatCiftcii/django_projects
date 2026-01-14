from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def login_request(request):
    
    if request.user.is_authenticated: # bu sessionid  alıyor login tekrar yapmamızı sağlıyor
        return redirect("products")
    if request.method=="POST":
        username=request.POST["username"]
        password=request.POST["password"]
        
        user = authenticate(request, username=username,password=password)
        if user is not None:
            login(request,user)
            nextUrl= request.GET.get("next", None) # yetki olmayan yerlerde login olmadıysak ve sonra login olduysak o anki login olmadığımız yuetkilenmediğimiz yere gideriz.
            if nextUrl is None:
                return redirect("products")
            else:
                return redirect(nextUrl)
        else:
            return render(request, "account/login.html",{
            "error":"username yada parola yanlış"
            })
        
    else:
        return render(request, "account/login.html")
    

def register_request(request):
    if request.method == "POST":
        username= request.POST["username"]
        email= request.POST["email"]
        password= request.POST["password"]
        repassword= request.POST["repassword"]
        
        if password == repassword:
            if User.objects.filter(username=username).exists(): #exits tru yada false dönderirir bu kullancıya ait başka kullanıc varmı diye sorar
                return   render(request, "account/register.html",{
                "error":"Username kullanılıyor."
            })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "account/register.html",{
                        "error":"bu email kullanılıyor."
            })
                else:
                    user=User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect("login")
                    
        else:
            return render(request, "account/register.html",{
                "error":"Parola eşleşmiyor"
            })
        
    else:
        return render(request, "account/register.html")

def logout_request(request):
    logout(request)
    return redirect("products")