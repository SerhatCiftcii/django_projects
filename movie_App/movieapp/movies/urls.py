from django.urls import path
from . import views


urlpatterns = [
        path("",views.index),
        path("movies",views.movies),
        # movies/1(film-adi) slug tüeü uyuyorsa hata vermez tipi ve ismi slug:slug oluyor
        path("movies/<slug:slug>",views.movies_details)
]
    
