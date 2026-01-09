from unicodedata import name
from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.shortcuts import redirect,render
from django.urls import reverse
import datetime
from .models import Product
from django.db.models import Avg,Min,Max
from django.template.context_processors import request

# Create your views here.
#


def index(request):
    # products=Product.objects.all().order_by("price")# fiyat a göre sıralama artan -dan yükseğe
    products=Product.objects.all().order_by("-price") #fiyat a göre sıralama azalan yükseğden -düşüğe

    product_max=Product.objects.aggregate(Max("price"))
    product_min=Product.objects.aggregate(Min("price"))
    context={
        "products":products,
    
        "max_price":product_max,
        "min_price":product_min
    }
    return render(request,'index.html',context)

def list(request):
    q = request.GET.get("q")  # .get() kullan, q yoksa None döner
    if q:  # q boş veya None değilse filtre uygula
        products = Product.objects.filter(name__contains=q).order_by("-price")
    else:
        products = Product.objects.all().order_by("-price")

    return render(request, 'list.html', {
        "products": products
    })
def create(request):
    if request.method == "POST":
        product_name = request.POST.get("product_name")
        price = request.POST.get("price")
        description = request.POST.get("description")
        image_name = request.POST.get("imageUrl")
        slug = request.POST.get("slug")

        if product_name == "" or len(product_name) <= 10:
            return HttpResponse("Ürün adı en az 10 karakter olmalı")

        new_product = Product(
            name=product_name,
            price=price,
            description=description,
            imageUrl=image_name,
            slug=slug
        )
        new_product.save()

        return redirect("product_list")
            
        # if (product_name==""): Tek tek tanımlamak yerine error tanımlamasıyla yapcaz
        #     return render(request, "create.html", {
        #         "error": "Product name is required."
        #         })
       

    return render(request, "create.html")

def details(request, slug):
    product = Product.objects.filter(slug=slug).first()
    categories=product.categories.all()
    # if not product:
    #     return HttpResponseNotFound("Ürün bulunamadı")
    # if not product:
    #      return HttpResponseNotFound("Ürün bulunamadı")

    return render(request, "details.html", {
        "product": product,
        "categories":categories
    })
    


        



# def telefon(request):
#     return HttpResponse("telefon kategorisindeki  ürünler")

# def bilgisayar(request):
#     return HttpResponse("bilgisayar kategorisindeki  ürünler")
   
