from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

 
    def __str__(self):
                return 'This is ' +self.name 


class Product(models.Model):
    name = models.CharField(max_length=50)
    price = models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(max_length=200, default='' , null=True , blank=True)
    image = models.ImageField(upload_to='images/')
    slug = models.CharField(max_length=200)

    def __str__(self):
                return 'This is ' +self.name 

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products()
    
   

class Payment(models.Model):
        sno = models.AutoField(primary_key=True)
        name = models.CharField(max_length=255)
        phone = models.CharField(max_length=12)
        address = models.CharField(max_length=255)
        mode = models.CharField(max_length=255)
        size = models.IntegerField(default=32, null=True)
        payment_status = models.BooleanField(default=False)
        delivered = models.BooleanField(default=False)

        def __str__(self):
                return 'Product brought by ' +self.name 


 
   