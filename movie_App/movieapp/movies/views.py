from django.shortcuts import HttpResponse, render


# Create your views here.
def index(request):
    return render(request, "index.html")
def movies(request):
     return render(request, "movies.html")
def movies_details(request , slug):
     return render(request, "movie-details.html", {
         "slug": slug}) # http://127.0.0.1:8000/movies/filmadi burda film adını ekrana basıyor. boşluk olmuycak hata atar
    