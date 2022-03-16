from django.http import HttpResponseRedirect
from django.shortcuts import render

import time
from rest_framework.decorators import api_view
from rest_framework.response import Response
from product.models import Product
from .serializer import *
from .models import *

# Create your views here.





# Create your views here.
@api_view(["GET"])
def get_panier(request):
    try:
        farmer = Panier.objects.all()
    except farmer.DoesNotExist:
        farmer = None
    serializer = PanierSerializer(farmer, many=True)
    return Response(serializer.data)



@api_view(["POST"])
def create_panier(request): 
    try: 
        panier =  Panier.objects.create() 
    except Panier.DoesNotExist: 
        panier =None 
    
    if panier : 
        serializer = PanierSerializer(panier, many=True)
        return Response(serializer.data)
    return  None



@api_view(["POST"])
def create_panier(request):  
    id  =  request.data['id'] 
    try: 
        panier =  Panier.objects.get(id=id) 
    except Panier.DoesNotExist: 
        panier =None  
    if panier: 
        for elm  in  request.data['article']  :  
            try : 
                article  =  Product.objects.get(id=elm.id) 
            except Product.doesNotExist: 
                return  Response({"error" :  "this is impossible"})
            try :  
                article_v = Article_vendu.objects.create(quantite = elm.quantite, article = article)
            except Article_vendu.DoesNotExist:
                article= None       
        serializer=PanierSerializer(panier)    
        return Response(serializer.data) 









