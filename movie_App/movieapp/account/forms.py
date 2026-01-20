# öncedn usernama ve password vardı yada email burda email ve ekstra hiç djangoda olmayan rememberı buraya  eklceiz benım anladığım username passwrodn emaial hazır , ama remember yok
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    email= forms.EmailField(widget=forms.EmailInput(attrs={"class":"form-control form-user", "placeholder":"EnterEmailadress."}))
    password = forms.CharField(widget= forms.PasswordInput(attrs={"class":"form-control form-user", "placeholder":"Enter Password"}))
    remember_me=forms.BooleanField(required=False,initial=False, widget=forms.CheckboxInput(attrs={"class":"custom-control-input"})) # seçilmezse fals gelir initail o required bi alanda değil zaten

    def clean_email(self):
        email=self.cleaned_data.get("email")
        
        if not User.objects.filter(email=email).exists():
            self.add_error("email","Email ile kayıtlı kullanıcı yok")
        return email
        