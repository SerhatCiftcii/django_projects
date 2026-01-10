from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product
from .forms import ProductCreateForm
from django.db.models import Max
from django.db.models import Min

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

    if request.method == 'POST':
        form = ProductCreateForm(request.POST)

        if form.is_valid():
            p = Product(name= form.cleaned_data["product_name"], 
            description = form.cleaned_data["description"], 
            price= form.cleaned_data["price"], 
            imageUrl="1.jpg", 
            slug=form.cleaned_data["slug"])
            p.save()
            return HttpResponseRedirect("list") 
    else:
        form = ProductCreateForm()
        
    return render(request, "create.html", {
        "form": form
    })

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
   
