from django.urls import path
from . import views
urlpatterns = [
    path('',  views.index, name='index'),     # ikisindede index gelir 
    path('index',  views.index, name='index'),

    path('details',  views.details, name='details'),
    path('list',  views.list, name='list'),
    
    # path('telefon', views.telefon), bu iki methoda ihityaç kalmadı 
    # path('bilgisayar', views.bilgisayar), 


    # path('<category>', views.getProductsByCategory) # int str sırasına dikkat et inmt yukarda olmazsa ilk str olan çalışıp hataya düşüyor.
     path('<int:category>', views.getProductsByCategoryId),
     path('<str:category>', views.getProductsByCategory)
    
     #kategorinin tipini belirleyebiliriz
     #kategorinin tipini belirleyebiliriz
    
]
