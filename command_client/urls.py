from django.urls import path
from .views import *

urlpatterns = [
    path('get_all', get_panier, name="create_farmer"),
    path('create_panier',create_panier , name="create_panier"),
]
