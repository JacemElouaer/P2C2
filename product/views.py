import time
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serialisers import *
from .models import * 

# Create your views here.
@api_view(["GET"])
def get_product(request):
    try:
        product = Product.objects.all()
    except product.DoesNotExist:
        product = None
    serializer = productSerializer(product, many=True)
    return HttpResponse(serializer.data)

@api_view(["POST"])
def create_product(request):
    data = request.data
    time.sleep(1)
    print("this is id :  ", id)
    
    product = Product.objects.create(
        nameProduct = data['nameProduct'],
        descriptionProduct = data['descriptionProduct'],
        priceProduct = data['priceProduct'],
        imageProduct= data['imageProduct']
    )
    serializer = productSerializer(product)
    print(serializer.data)
    return Response(serializer.data)

@api_view(["PUT"])
def update_product(request): 
    data = request.data
    product = Product.objects.get(id=request.data['id'])
    serializer = productSerializer(instance=product, data=data)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(["POST"])
def delete_product(request):
    product = Product.objects.get(id=request.data['id'])
    product.delete()
    return Response("Product was deleted")