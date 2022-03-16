from  django.shortcuts import render 
from  rest_framework.decorators import api_view  
from  rest_framework.response import Response 
from .models import * 
from .serializer import *

# Create your views here.



@api_view(["GET"])
def get_pc_by_id(request): 
    id = request.data["id"]
    try:
        pcCol = PointCollection.objects.get(id=id)
    except PointCollection.DoesNotExist:
        pcCol = None
    if pcCol:
        serializer = PCSerializers(pcCol, many=False)
        return Response(serializer.data)
    return Response({"Error": "There is not  Admin  with  this id"})


@api_view(["GET"])
def get_pc_by_manager_id(request):
    id = request.data['id'] 
    try : 
        manager  =  Admin.objects.get(id=id)
    except Admin.DoesNotExist:
        manager = None
    if manager : 
        try:
            pcCol = PointCollection.objects.get(manager=manager)
        except PointCollection.DoesNotExist:
            pcCol = None
        if pcCol:
            serializer = PCSerializers(pcCol, many=False)
            return Response(serializer.data)
        return Response({"Error": "There is not  Admin  with  this id !!"})
    return Response({"Error": "manager does not exist !!"}) 





@api_view(["POST"])
def create_PCCollection(request):
    data = request.data
    try : 
        manager  =  Admin.objects.get(id=data['id'])
    except Admin.DoesNotExist:
        manager = None
    if manager : 
        pcCol = PointCollection.objects.create(
            name=data["name"],
            adresse=data["adresse"],
            manager =  manager
            )
        if isinstance(pcCol, PointCollection): 
            return Response({"success": "the point de collection is added successefully"})
        return Response({"Error": "he manager  has not be added"})
    return Response({"Error": "the manager dose not exist !! "}) 



@api_view(['GET'])
def index_pc(request):
    context={}
    return  render (request, "admin/consulterptod.html" , context)