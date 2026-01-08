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
    if request.GET["q"] and request.GET["q"] is not None:
        q=request.GET["q"]
        products=Product.objects.filter(name__contains=q).order_by("-price")
    else:
        return HttpResponseRedirect("/products")

    return render(request,'list.html',{
        "products":products
        })
def create(request):
    if request.method=="POST":
        product_name=request.POST["name"]
        price=request.POST["price"]
        description=request.POST["description"]
        image_name=request.POST["imageUrl"]
        slug =request.POST["slug"]

        # new_product=Product(
        #     name=product_name,
        #     price=price,
        #     description=description,
        #     imageUrl=image_name
        #     slug=slug
        # )
        # new_product.save()
        return redirect(reverse("myapp:index"))
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
   
