from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    if request.method == 'GET': 
        return  render(request, 'index.html' ) 
    
    
def login_client(request): 
    return  render(request, 'client/login.html'  )     