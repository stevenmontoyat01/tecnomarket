from datetime import datetime
from django.db import models

# Create your models here.

class Type_products (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Brands (models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class products (models.Model):
    type_product = models.ForeignKey(Type_products ,on_delete=models.CASCADE)
    brand = models.ForeignKey(Brands,on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    Manufacturing_date =models.DateField(default=datetime.now())
    image = models.ImageField(upload_to='products',null=True)
    price = models.IntegerField()
    units = models.IntegerField()

