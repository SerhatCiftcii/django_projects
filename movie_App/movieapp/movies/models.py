from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.fields import CharField


class Genre(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return f"[{self.id}] - {self.name}"

class Contact(models.Model):
    address=models.CharField(max_length=200)
    email=models.EmailField(null=True, blank=True)
    
    def __str__(self):
        return f"[{self.id}] - {self.address}"
      
class Person(models.Model):
    genders = (
        ('M', "Erkek"),
        ('F', "Kadın"),
    )
    duty_types = (
        ('1', "Görevli"),#filmde görev alan kişiler
        ('2', "Oyuncu"),#oyuncular
        ('3', "Yönetmen"),#yöetmen
        ('4', "Senarist"),#film senaryosu
    )

    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    biography=models.CharField(max_length=500)
    image_name=models.CharField(max_length=50)
    date_of_birth=models.DateField()
    gender=models.CharField("Cinsiyet",max_length=1,choices=genders)
    duty_type=models.CharField("Görev Tipi",max_length=1, choices=duty_types)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"
    full_name.fget.short_description = "Ad Soyad"
    class Meta:
        verbose_name="Kişi"
        verbose_name_plural = "Kişiler"
    
    def __str__(self):
        return f"[{self.id}] - {self.first_name} {self.last_name} ({self.duty_types[int(self.duty_type)-1][1]})"

# Create your models here.
class Movie(models.Model):
    title=models.CharField("Başlık",max_length=100)
    description=models.TextField("Açıklama",validators=[MinLengthValidator(20)]) # mutlaka 20 karakter olmalı
    image_name=models.CharField("Resim",max_length=50)
    image_cover=models.CharField("Kapak Resmi",max_length=50)
    date = models.DateField(null=True, blank=True)
    slug=models.SlugField(unique=True,db_index=True)
    budget=models.DecimalField("Bütçe",max_digits=15,decimal_places=2)
    language=models.CharField(max_length=30)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)
    is_active=models.BooleanField("Aktif Mi?",default=True)
    is_home=models.BooleanField("Ana Sayfa?",default=False)
    
    
    class Meta: # bu nedir? 
        verbose_name="Film"
        verbose_name_plural = "Filmler"
    
    def __str__(self):
        return f"[{self.id}] - {self.title}"


class Video(models.Model):
    title = models.CharField(max_length=100)
    url= models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    def __str__(self):
        return f"[{self.id}] - {self.title}"
    
    
    