from django.db import models

# Create your models here.

class Product(models.Model):
    nameProduct= models.CharField(null=False, max_length=30)
    descriptionProduct= models.TextField(null=False)
    priceProduct= models.FloatField(null=False)
    imageProduct= models.TextField(null=False)
    stock = models.IntegerField(default = 20 ,blank = True,  null=False)
    
    class Meta:
        db_table= 'table_product'