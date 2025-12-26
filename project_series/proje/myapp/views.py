from django.http import response, HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect,render
from django.urls import reverse
import datetime
# Create your views here.
#
data = {
    "telefon": ["samsungs20","apple10","oppo10pro"] ,
    "bilgisayar":["leptop1","leptop2"],
    "elektronik":[]
}
def index(request):
    # list_items=""
    categories=list(data.keys()) #key ve value üretir
    
    
    # for category in category_list:
    #     redirect_path= reverse("products_by_category", args=[category])
    #     list_items +=f" <li><a href=\"{redirect_path}\">{category} </a> </li>"
        
    # html= f"<ul>{list_items}</ul>"
    return render(request, 'index.html',{
        "categories":categories,
       
        
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
   
