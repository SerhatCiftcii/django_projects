from django.forms import widgets
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["full_name", "email", "text", "rating"]

        labels = {
            "full_name": "Ad Soyad",
            "email": "Eposta",
            "text": "Yorum",
            "rating": "Puan"
        }

        widgets = {
            "full_name": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "text": forms.Textarea(attrs={"class": "form-control"}),
            "rating": forms.Select(
        attrs={"class": "form-control custom-select"},
        choices=(
            ('', "Puan Seçiniz"), # Boş değer eklendi
            (1, "1 Yıldız"),
            (2, "2 Yıldız"),
            (3, "3 Yıldız"),
            (4, "4 Yıldız"),
            (5, "5 Yıldız"),
        )
    ),
        }
