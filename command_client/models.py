from django.db import models
from client.models import Client 
from product.models import Product
from pointCollection.models import  PointCollection

# Create your models here.

class Article_vendu(models.Model): 
    article =  models.ForeignKey(Product ,  on_delete=models.CASCADE)
    quantite =  models.IntegerField()  
    panier  = models.ForeignKey('Panier' , on_delete=models.CASCADE)  
    
class Panier(models.Model): 
    date_ajout =  models.DateField(auto_now_add=True)
    
    


class Command_Client(models.Model): 
    client  =  models.ForeignKey( Client ,on_delete=models.CASCADE) 
    point_collection =  models.ForeignKey( PointCollection, on_delete=models.CASCADE) 
    tarification   =  models.FloatField()
    id_panier = models.ForeignKey(Panier, on_delete=models.CASCADE)

    


