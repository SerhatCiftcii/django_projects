from django.urls import path

from . import views
urlpatterns = [
    path('',  views.index, name='index'),     # ikisindede index gelir 
    path('index',  views.index, name='index'),
    path('list',  views.list),
    path("create", views.create),



    # path('telefon', views.telefon), bu iki methoda ihityaç kalmadı 
    # path('bilgisayar', views.bilgisayar), 


    # path('<category>', views.getProductsByCategory) # int str sırasına dikkat et inmt yukarda olmazsa ilk str olan çalışıp hataya düşüyor.
    
    
    # path("<int:id>",views.details),
       path("<slug:slug>",views.details ,name="product_details"),#artık id ye göre bekleme değilde slug ile yapacağız eşleşmeyi viewsdada slug belirtcez id kaldırcaz

    
     #kategorinin tipini belirleyebiliriz
     #kategorinin tipini belirleyebiliriz
    
]
