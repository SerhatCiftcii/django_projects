from django.db import models
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=70)
    def __str__(self):
        return f" [{self.pk}] - {self.name}"
    
class Adress(models.Model):
    street=models.CharField(max_length=100)
    postal_code=models.CharField(max_length=5)
    city=models.CharField(max_length=50)
    def __str__(self):
        return f"{self.street} - {self.city} - {self.postal_code}"
class Supplier(models.Model):
    company_name=models.CharField(max_length=100)
    address=models.OneToOneField(Adress, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return f"{self.company_name}"

    
class Product(models.Model):
    name= models.CharField(max_length=50) # varchar max 50 sql karşılığı
    price = models.DecimalField( max_digits=8, decimal_places=2)
    description=models.CharField(max_length=200)
    image = models.FileField(upload_to="images/", blank=True, null=True)
    
    isActive= models.BooleanField(default=True)#NULL =>null=True DEĞER içeriz herhangi bir kayıt olmaz yani 0 yada 1 olarak gelmez, illa true false olmasına gerek yok
    #eğer ya true yada false olmasını istiyorsak default olarak default=True dersek 1 olur yada false dersek 0 olur
    
    """category=models.ForeignKey(Category, on_delete=models.CASCADE,null=True, related_name="products") # ilişki kurduk category ile burda , bir kategori silinirse ona bağlı ürünlerde silinsin istiyoruz on_delete=models.CASCADE ile , null=True bu alan boş geçilebilir demek..////Cascade yerine on_delete=models.SET_NULL da kullanılabilir bu durumda kategori silinirse ürün kalır ama kategorisi null olur null=true olması gerek ama dikkat bunu tanımlarsan, yada setdafult bi değer///"""
    supplier=models.ForeignKey(Supplier, on_delete=models.CASCADE, null=True,) 
    categories=models.ManyToManyField(Category) #bir ürün birden fazla kategoriye ait olabilir bir kategoriye de birden fazla ürün ait olabilir many to many ilişki kurduk
    
    # category=models.CharField(max_length=50, null=True) # null kabul edilmeyen değer boş string gönderme 
    # # buraya dikkat et null kısmı db_index ksımını furkanla konuş 
    
    slug =models.SlugField(default="", null=False, db_index=True ,blank=True) #mig olucak bunun için name göre bi veri bulcaz /1 yerine products/telefonu bulcaz bunun sayesinde zaten otomatik oluşuyor sluga adminde görmemek için editable create aşamsında o kendi kendiine oluşcak zaten
    
    
    #*******Önemli*** slug methodu artık biz ürün oluşturduktan sonra otomatık veri tabnanına name alanıyla aynı olcak şekilde slug alanını doldurcak.her slug fakrlı name göre olcak aynı isimde hata vermemesi için unique=True dedik
    """ 
    def save(self, *args, **kwargs):
        # self.slug= self.name.replace(" ","-").lower() #  bu yapı yerine yada boşlukları silin türkçe akrakterleri ing yapn çeviren bir yapıyı kullancaz slugify bu yapida
        self.slug= slugify(self.name)
        super().save(*args, **kwargs)
    """
        
    def __str__(self):
        return f"{self.name} - {self.price}"
    
class UploadModel(models.Model):
    image = models.FileField(
    upload_to="images/",
    blank=True,
    null=True
) # dosya isminin saklnması imagefield de kullanılabilir.iamge için
        
    