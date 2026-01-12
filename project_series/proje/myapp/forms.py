from django import forms
# class ProductCreateForm(forms.Form):
#     product_name = forms.CharField(
#         label="Ürün Adı",
#         min_length=2,
#         error_messages={
#             "min_length": "Ürün adı en az 2 karakter olmalıdır."
#         },
        
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )

#     price = forms.DecimalField(
#         label="Fiyat",
#         widget=forms.NumberInput(attrs={"class": "form-control"})
#     )

#     description = forms.CharField(
#         label="Açıklama",
#         widget=forms.Textarea(attrs={
#             "class": "form-control",
#             "rows": 4
#         })
#     )

#     slug = forms.SlugField(
#         label="Slug",
#         widget=forms.TextInput(attrs={"class": "form-control"})
#     )

# modelse göre tanımlama alttaki gibi
class ProductForm(forms.ModelForm): # genel form yapısı
# class ProductCreateForm(forms.ModelForm): # modellerle form karışık aslında ordan türyücek
    class Meta:
        from .models import Product
        model = Product
        error_messages = {
            'name': {
                "required": "name alanını giriniz",
                'max_length': "Ürün adı en fazla 50 karakter olmalıdır.",
            },
            'price': {
                "required": "price alanın sayısal değer giriniz",
                "invalid": "Geçersiz fiyat değeri. sayısal değer giriniz",
                
            },
        }
        fields = ["name", "price", "description", "slug"] #hangi alanları kullanmak istiyorsak onları yazcaz
        labels = {
            "name": "Ürün Adı",
            "price": "Fiyat",
            "description": "Açıklama",
            "slug": "Slug"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.TextInput(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "slug": forms.TextInput(attrs={"class": "form-control"})
        }
class UploadForm(forms.Form):       
    image=forms.FileField()
    