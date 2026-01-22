from django.shortcuts import redirect, render
from django.template.context_processors import request
from django.contrib.admin import register
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


from account.forms import CreateUserForm, LoginForm
from movies.models import Movie
# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    if request.method == "POST":
        form = LoginForm(request.POST)
        
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            remember_me=form.cleaned_data.get("remember_me")
            username= User.objects.get(email=email).username
            user = authenticate(username=username, password=password)
           
            
            if user is not None:
                login(request, user)
                if not remember_me:
                    request.session.set_expiry(0)
                    request.session.modified=True
                return redirect("home_page")
            else:
                form.add_error(None, "email yada parola yanlıştır")
                return render(request, "account/login.html",{
                    "form":form
                })
        else:
            return render(request,"account/login.html",{
                "form":form
            })
    form = LoginForm()
    return render(request, "account/login.html",{
        "form":form
    })
    
def register_request(request):
    # 1. ADIM: Kullanıcı zaten giriş yapmışsa hemen gönder (Boşuna formla uğraşmasın)
    if request.user.is_authenticated:
        return redirect("home_page")

    # 2. ADIM: İstek türüne bakıyoruz (Veri mi gönderildi yoksa sayfa mı açılıyor?)
    if request.method == "POST":
        # 3. ADIM: Kutuyu (Formu) kullanıcının gönderdiği (POST) verilerle dolduruyoruz.
        # Bu aşamada veriler hala "HAM" (kirli) haldedir.
        form = CreateUserForm(request.POST)

        # 4. ADIM: İŞTE BURASI KRİTİK! is_valid() çağrıldığı an Django şunları yapar:
        #   a) Veri tipleri doğru mu? (Email gerçekten email mi?)
        #   b) Senin yazdığın "clean_email" fonksiyonunu çalıştırır.
        #   c) UserCreationForm'un kendi içindeki "şifreler eşleşiyor mu?" kontrolünü yapar.
        if form.is_valid():
            # 5. ADIM: Eğer yukarıdaki tüm kontrollerden GEÇTİYSE buraya girer.
            # form.save() diyerek veritabanına yeni kullanıcıyı yazarız.
            user = form.save()
            
            # 6. ADIM: Kayıttan sonra kullanıcıyı otomatik içeri alalım (Login).
            # Dikkat: authenticate için ham şifre gerekir. 
            # form.cleaned_data['password1'] artık güvenli ve hazırdır.
            #Neden buradayız? Çünkü kullanıcıyı kayıt ettikten sonra 
# tekrar "Giriş Yap" sayfasına yollayıp uğraştırmak istemiyoruz. direkt login 

            # username = form.cleaned_data.get("username")
            username=user.username
            password = form.cleaned_data.get("password1")
            
            user = authenticate(username=username, password=password)
            if user is not None:# İşte şimdi tarayıcıya "BU KİŞİYİ TANI" çerezini (cookie) bıraktık.
                login(request, user)
                return redirect("home_page")
        
        else:
            # 7. ADIM: is_valid() başarısız olduysa (Örn: Email zaten var)
            # Django hata mesajlarını formun içine otomatik yerleştirdi.
            # Biz sadece formu tekrar sayfaya gönderiyoruz.
            return render(request, "account/register.html", {"form": form})

    # 8. ADIM: Eğer metod GET ise (Sayfa ilk kez açılıyorsa)
    # Bomboş, tertemiz bir form örneği oluşturuyoruz.
    else:
        form = CreateUserForm()
    
    return render(request, "account/register.html", {"form": form})
    

def change_password(request):
    return render(request,"account/change_password.html")
def profile(request):
   
    return render(request,"account/profile.html")
def watch_list(request):
    return render(request,"account/watch_list.html")

def logout_request(request):
    logout(request)
    return redirect("home_page")

