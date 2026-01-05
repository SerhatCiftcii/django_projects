from django.db import models
from django.core.validators import MinLengthValidator
from django.db.models.fields import CharField
 


class Genre(models.Model):
    name=models.CharField(max_length=100)

class Contact(models.Model):
    address=models.CharField(max_length=200)
    email=models.EmailField(null=True, blank=True)
      
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
    gender=models.CharField(max_length=1,choices=genders)
    duty_type=models.CharField(max_length=1, choices=duty_types)
    contact = models.OneToOneField(Contact, on_delete=models.CASCADE, null=True, blank=True)


# Create your models here.
class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(validators=[MinLengthValidator(20)]) # mutlaka 20 karakter olmalı
    image_name=models.CharField(max_length=50)
    image_cover=models.CharField(max_length=50)
    date = models.DateField(),
    slug=models.SlugField(unique=True,db_index=True)
    budget=models.DecimalField(max_digits=15,decimal_places=2)
    language=models.CharField(max_length=30)
    people = models.ManyToManyField(Person)
    genres = models.ManyToManyField(Genre)
    

    
class Video(models.Model):
    title = models.CharField(max_length=100)
    url= models.CharField(max_length=200)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    
    