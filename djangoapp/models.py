# from django.db import models

# # Create your models here.

# class DressCategory(models.Model):
#     category_name = models.CharField( max_length=200)


# class DressDetails(models.Model):
#     dress_name = models.CharField( max_length=200)
#     dress_price = models.CharField( max_length=200)
#     dress_image = models.URLField( max_length=6000)
#     dress_category = models.ForeignKey("DressCategory,on_delete=models.CASCADE")

from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='products/')
   

    def __str__(self):
        return self.title