from django.http import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect, response
from django.shortcuts import redirect,render
from django.urls import reverse
import datetime
from .models import Product
# Create your views here.
#
data = {
    "telefon": ["samsungs20","apple10","oppo10pro"] ,
    "bilgisayar":["leptop1","leptop2"],
    "elektronik":[]
}
def index(request):
    products=Product.objects.all()
    context={
        "products":products
    }
    return render(request,'index.html',context)


def details(request, slug):
    product = Product.objects.filter(slug=slug).first()

    # if not product:
    #     return HttpResponseNotFound("Ürün bulunamadı")
    # if not product:
    #      return HttpResponseNotFound("Ürün bulunamadı")

    return render(request, "details.html", {
        "product": product
    })
    

def getProductsByCategoryId(request , category_id):
    ids = list(data.keys())
    if category_id > len(ids):
        return HttpResponseNotFound("yanlış kategori seçimi")
    category_name = ids[category_id-1]
    redirect_path= reverse("products_by_category", args=[category_name])
    return redirect( redirect_path)
   
   
    # return HttpResponseRedirect("") eski kullanım yenide redirect var kısa
    

def getProductsByCategory(request,category):
    try:
         products=data[category]
         
         return render(request,'products.html',{
             "category":category,
              "urunler": products,
              "now":datetime.datetime.now()
             
         })
    except:
        return HttpResponseNotFound(f"<h1> yanlış kategori seçimi </h1>")
        
        



# def telefon(request):
#     return HttpResponse("telefon kategorisindeki  ürünler")

# def bilgisayar(request):
#     return HttpResponse("bilgisayar kategorisindeki  ürünler")
   
