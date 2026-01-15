from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User
from django.forms import ValidationError, forms, widgets
from django.contrib import messages

 #burda aslında bu sınıfa kalıtım yoluyla alıyoruz hazır yapının üstüne ekstra alan veya değişim yapoabilceiz
class LoginUserForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        self.fields["username"].widget = widgets.TextInput(attrs={"class":"form-control"}) # widgetsi eziyoruz burda 
        self.fields["password"].widget = widgets.PasswordInput(attrs={"class":"form-control"})
        
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if username == "admin":
            messages.error(self.request,"Hoşgeldin Admin")
        return username
    def confirm_login_allowed(self, user):
        if user.username.startswith("s"): #username s le başlıyorsa bu hatayı verir
            raise forms.ValidationError("bu kullanıcı adıyla login olmazsınız")
        return super().confirm_login_allowed(user)

class NewUserForm(UserCreationForm):
    class Meta:
        model = User
        fields= ("username","email")
        
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)
        self.fields["password1"].widget= widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["password2"].widget= widgets.PasswordInput(attrs={"class":"form-control"})
        self.fields["username"].widget= widgets.TextInput(attrs={"class":"form-control"})
        self.fields["email"].widget= widgets.EmailInput(attrs={"class":"form-control"})
        self.fields["password1"].required= True
    def clean_email(self):
        email=self.cleaned_data.get("email")
        
        if User.objects.filter(email = email).exists():
            self.add_error("email", "email daha önce kullanılmıştır")

         
        
        
        
        
            
        
