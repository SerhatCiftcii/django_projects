from django.contrib.auth.forms import UserCreationForm
# öncedn usernama ve password vardı yada email burda email ve ekstra hiç djangoda olmayan rememberı buraya  eklceiz benım anladığım username passwrodn emaial hazır , ama remember yok
from django import forms
from django.contrib.auth.models import User
from django.forms import fields, widgets
import random

class LoginForm(forms.Form):
    email= forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control form-user", "placeholder":"EnterEmailadress."}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class":"form-control form-user", "placeholder":"Enter Password"}))
    remember_me=forms.BooleanField(required=False,initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"})) # seçilmezse fals gelir initail o required bi alanda değil zaten

    def clean_email(self):
        email=self.cleaned_data.get("email")
        
        if not User.objects.filter(email=email).exists():
            self.add_error("email","Email ile kayıtlı kullanıcı yok")
        return email
    
class CreateUserForm(UserCreationForm): 
    class Meta:
          model=User
          fields= ("email","first_name","last_name",)#usera yar random ayda firstanem giresin 
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget=widgets.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Password Again"})
        self.fields["password2"].widget=widgets.PasswordInput(attrs={"class":"form-control form-control-user","placeholder":"Password2 Again"})
        
        self.fields["first_name"].widget=widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"first_name"})
        self.fields["last_name"].widget=widgets.TextInput(attrs={"class":"form-control form-control-user","placeholder":"last_name"})
        
        
        self.fields["email"].widget=widgets.EmailInput(attrs={"class":"form-control form-control-user","placeholder":"Email"})
        self.fields["email"].required=True
        self.fields["first_name"].required=True
        self.fields["last_name"].required=True
        
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        
        # Email boş gelmişse (required=True olmasına rağmen garantiye alalım)
        if not email:
            return email

        # Veritabanında kontrol et
        if User.objects.filter(email=email).exists():
            # self.add_error yerine genellikle ValidationError fırlatılır ama add_error da olur
            raise forms.ValidationError("Bu email adresi zaten kullanımda.")
            
        return email # MUTLAK kural: Temizlenmiş veriyi geri döndürmelisin!
    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        user.username = "{}_{}_{}".format(
            self.cleaned_data.get("first_name").replace("ı","i").replace("ö","o").lower(),
            self.cleaned_data.get("last_name").lower(),
            random.randint(11111,99999)
        )
        if commit:
            user.save()
        
        return user