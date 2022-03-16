from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="home_app"), 
    path('login_client' ,  login_client , name ="login_client")
]
