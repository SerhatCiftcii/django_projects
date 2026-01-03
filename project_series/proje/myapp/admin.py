from django.contrib import admin
from django.utils.html import escape
from django.contrib.admin import register
from .models import Product ,Category, Supplier, Adress




class ProductAdmin(admin.ModelAdmin):
    list_display = ("name","price","isActive","selected_categories",) #admin panelinde listeleme yaparken hangi alanları göstereceğimizi belirtiyoruz
    # readonly_fields=("slug",) # fiyat alanını sadece okunur yapıyoruz admin panelinde düzenlenmesini engelliyoruz
    prepopulated_fields=({"slug":("name",)}) # slug alanını name alanına göre otomatik dolduruyoruz models içindeki **save** metodunu kullanmanın artık bi anlamı kalmadı onu yorum satırı yapıyorum.
    list_display_links=("name",) # listeleme ekranında hangi alanlara tıklanabilirlik ekleyeceğimizi belirtiyoruz
    list_filter=("isActive","categories") # filtreleme seçenekleri ekliyoruz admin panelinde sağ tarafta
    list_editable=("isActive",) # listeleme ekranında isActive alanını düzenlenebilir yapıyoruz 
    search_fields=("name",) # arama çubuğunda hangi alanlarda arama yapılacağını belirtiyoruz
    def selected_categories(self,obj):
        html=""
        for category in obj.categories.all():
           html +=category.name + ", "
        return html
admin.site.register(Product,ProductAdmin)# yönetim panelinie ekledik productı
# Register your models here.
admin.site.register(Category)
admin.site.register(Supplier)
admin.site.register(Adress)

