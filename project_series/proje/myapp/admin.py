from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","isActive","category") #admin panelinde listeleme yaparken hangi alanları göstereceğimizi belirtiyoruz
    readonly_fields=("slug",) # fiyat alanını sadece okunur yapıyoruz admin panelinde düzenlenmesini engelliyoruz
    
    list_display_links=("name",) # listeleme ekranında hangi alanlara tıklanabilirlik ekleyeceğimizi belirtiyoruz
    
    
    list_filter=("isActive","category") # filtreleme seçenekleri ekliyoruz admin panelinde sağ tarafta
    list_editable=("isActive",) # listeleme ekranında isActive alanını düzenlenebilir yapıyoruz 
    search_fields=("name","category") # arama çubuğunda hangi alanlarda arama yapılacağını belirtiyoruz

admin.site.register(Product,ProductAdmin)# yönetim panelinie ekledik productı
# Register your models here.
