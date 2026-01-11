from django.contrib import messages
from django.http.response import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from .models import Product
from .forms import ProductForm
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
    
    #Alternatif Yöntem else yerine
    # if request.method == 'GET':
    #     form = ProductCreateForm()

    if request.method == 'POST':
        form = ProductForm(request.POST)

        if form.is_valid(): # modelse göre validasyon yapar 2.yöntem alltaki yazdıklarımızla uğraşmıyoruz.
            # p = Product(name= form.cleaned_data["product_name"], 
            # description = form.cleaned_data["description"], 
            # price= form.cleaned_data["price"], 
            # imageUrl="1.jpg", 
            # slug=form.cleaned_data["slug"])
            form.save()
            # messages.success(request, "Ürün başarıyla eklendi")
            return HttpResponseRedirect("list")
    else:
        form = ProductForm()
        
    return render(request, "create.html", {
        "form": form
    })
def edit(request,id):
    product = get_object_or_404(Product, pk=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect(reverse('product_details', args=[product.slug]))
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit.html', {
        'form': form,
        'product': product
    })
def delete(request,id):
    product = get_object_or_404(Product, pk=id)
    
    if request.method == 'POST':
        product.delete()
        return redirect('product_list')
    return render(request, 'delete-confirm.html', {
        'product': product
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
   
