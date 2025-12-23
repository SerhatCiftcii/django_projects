from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect,render

# Create your views here.

#
def index(request):
    return HttpResponse("merhaba")

def details(request):
    return HttpResponse("details")

def list(request):
    return HttpResponse("list")

def getProductsByCategoryId(request , category):
    return redirect("/products/telefon")


def getProductsByCategory(request,category):
    category_text=None
    if category =='bilgisayar':
        category_text="bilgisayar kategorisinden ürünler"
    elif category =='telefon':
        category_text = "telefon kategorisindeki ürünler"
    else:
        category_text = "yanlış kategori seçimi"
    return HttpResponse(category_text)



# def telefon(request):
#     return HttpResponse("telefon kategorisindeki  ürünler")

# def bilgisayar(request):
#     return HttpResponse("bilgisayar kategorisindeki  ürünler")
    
