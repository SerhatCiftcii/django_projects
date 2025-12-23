"""
URL configuration for examples project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
# path('', include('myapp.urls')),   böyle olursa alltaki gibi olur myyappde tanımalnanlar vs ama 2.kısım
# index=> details yada list tarafı boş oldu için path otomatik includden gelcek
#http80:80/details
#http80:80/list 


#2. kısım
#http80:80/products/details

urlpatterns = [
    path('products/', include('myapp.urls')),
    path('admin/', admin.site.urls),
]
