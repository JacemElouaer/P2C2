from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializer import *
from .selectors import *
from .services import *
from django.views.generic import TemplateView 
from django.contrib.auth import authenticate, login, logout 
from pointCollection.models import PointCollection  
from pointCollection.serializer import *
from product.models import *  
from  product.serialisers import productSerializer


# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def create_client(request):
    data =  request.data
    client_data =  data['client']
    user = Account.objects.create(
        email=data["email"],
        name=data["name"],
        password =  data['password'],
        is_active=True,
        is_staff=False
    )
    if isinstance(user, Account):
        client = Client(user=user, first_name=client_data['first_name'],
                        last_name=client_data['last_name'], telephone=client_data['telephone'])
        client.save()
        serializer = ClientSerializers(client, many=False)
        return Response(serializer.data)
    return  Response({"error" :  "the client didn't add"})


@api_view(['GET'])
@permission_classes([AllowAny])
def get_clients(request):
    try:
        clients = Client.objects.all()
    except Client.DoesNotExist:
        clients = None
    if clients:
        print(clients)
        serialiszer = ClientSerializers(clients, many=True)
        return Response(serialiszer.data)
    return Response({"error": "there is no clients in the Database"})

@api_view(['GET'])
@permission_classes([AllowAny])
def get_client_by_id(request):
    data = request.data
    id = data['id']
    try:
        client = Client.objects.get(id=id)
    except Client.DoesNotExist:
        client = None
    if client:
        serialiszer = ClientSerializers(client, many=False)
        return Response(serialiszer.data)
    return {"error": "there is no clients in the Database"}





@api_view(['GET'])
@permission_classes([AllowAny])
def get_client_by_email(request):
    data = request.data
    email = data['email']
    try:
        client = Client.objects.get(email =  email)
    except Client.DoesNotExist:
        client = None
    if client:
        serialiszer = ClientSerializers(client, many=False)
        return Response(serialiszer.data)
    return {"error": "there is no clients in the Database"}



class LoginView(TemplateView):
    
  template_name = 'client/login.html'

  def post(self, request, **kwargs):

    username = request.POST.get('username', False)
    password = request.POST.get('password', False)
    user = authenticate(username=username, password=password)
    if user is not None and user.is_active:
        login(request, user)
        return HttpResponseRedirect( "client/index.hmtl" )

    return render(request, self.template_name)

class LogoutView(TemplateView):
    
  template_name = 'front/index.html'

  def get(self, request, **kwargs):

    logout(request)

    return render(request, self.template_name)







def index(request):
    
    try:
        pcCol = PointCollection.objects.all()
    except PointCollection.DoesNotExist:
        pcCol = None
    if pcCol :
        ser  = PCSerializers(pcCol , many=True)
        context = {"pc" :ser.data }
        return render(request, 'client/index.html' ,  context)
    return HttpResponse("none")



def afficher_product(request):  
    try:  
        products  =  Product.objects.all() 
    except Product.DoesNotExist:
        return  None
    if products:
        ser =  productSerializer(products , many=True)
    context = {'products': ser.data}
    return render(request ,'client/produits.html' , context )
    