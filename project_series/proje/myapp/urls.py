from django.urls import path
from . import views
urlpatterns = [
    path('',  views.index, name='index'),     # ikisindede index gelir 
    path('index',  views.index, name='index'),



    # path('telefon', views.telefon), bu iki methoda ihityaç kalmadı 
    # path('bilgisayar', views.bilgisayar), 


    # path('<category>', views.getProductsByCategory) # int str sırasına dikkat et inmt yukarda olmazsa ilk str olan çalışıp hataya düşüyor.
     path('<int:category_id>', views.getProductsByCategoryId),
     path('<str:category>', views.getProductsByCategory ,name='products_by_category')
    
     #kategorinin tipini belirleyebiliriz
     #kategorinin tipini belirleyebiliriz
    
]
