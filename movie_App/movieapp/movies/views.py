from datetime import date
from django.shortcuts import get_object_or_404, render
from django.http.response import HttpResponseRedirect
from django.urls import reverse

from movies.forms import CommentForm
from movies.models import Movie

data = {   
    "sliders": [
        {
            "slider_image": "slider1.jpg",
            "url": "film-adi-1"
        },
         {
            "slider_image": "slider2.jpg",
            "url": "film-adi-2"
        },
         {
            "slider_image": "slider3.jpg",
            "url": "film-adi-3"
        }
    ]
}

# Create your views here.

def index(request):
    movies = Movie.objects.filter(is_active=True,is_home=True)
    sliders = data["sliders"]
    return render(request, 'index.html', {
        "movies": movies,
        "sliders": sliders
    })

def movies(request):
    movies = Movie.objects.filter(is_active=True)
    return render(request, 'movies.html', {
        "movies": movies
    })


def movie_details(request, slug):
    movie = get_object_or_404(Movie, slug=slug)
    
    # POST isteği varsa bu blok çalışır
    if request.method == "POST":
        comment_form = CommentForm(request.POST) # Veriyi buraya aldık
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.movie = movie
            comment.save()
            return HttpResponseRedirect(reverse("movie_details", args=[slug]))
        # EĞER HATA VARSA (is_valid False ise) kod buradan devam eder
        # comment_form şu an içinde hata mesajlarını (email zorunludur vs.) tutuyor.
    
    else:
        # Sayfa ilk kez açılıyorsa boş form oluşturur
        comment_form = CommentForm()

    # BURASI KRİTİK: Eğer POST başarısız olduysa, içindeki hatalarla birlikte 
    # comment_form değişkenini render'a gönderiyoruz.
    return render(request, 'movie-details.html', {
        "movie": movie,
        "genres": movie.genres.all(),
        "people": movie.people.all(),
        "videos": movie.video_set.all(),
        "comment_form": comment_form # Hatayı taşıyan form buraya gidiyor
    })