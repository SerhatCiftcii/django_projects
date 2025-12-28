from django.db import models

# Create your models here.

class Product(models.Model):
    name= models.CharField(max_length=50) # varchar max 50 sql akrşılığı
    price = models.DecimalField( max_digits=8, decimal_places=2)
    description=models.CharField(max_length=200)
    imageUrl=models.CharField(max_length=50)
    isActive= models.BooleanField(default=True)#NULL =>null=True DEĞER içeriz herhangi bir kayıt olmaz yani 0 yada 1 olarak gelmez, illa true false olmasına gerek yok
    #eğer ya true yada false olmasını istiyorsak default olarak default=True dersek 1 olur yada false dersek 0 olur
    category=models.CharField(max_length=50, null=True)
    def __str__(self):
        return f"{self.name} - {self.price}"