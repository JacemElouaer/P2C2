from django.urls import path
from .views import *


urlpatterns = [
    # les urls des devis appartment
    path('create_client/', create_client , name="create_client"),
    path('get_clients/', get_clients, name="get_all_clients"),
    path('get_client_by_id/', get_client_by_id, name="get_client_by_client"),
    path('get_client_by_email/', get_client_by_email, name="get_client_by_client"),
    path('login_client/', LoginView.as_view(), name="login_client"),
    path('logount/', LogoutView.as_view(), name="logout_client"), 
    path('client_index' ,  index ,  name="index_client"),
    path('product/' ,  afficher_product ,  name="afficher_product")
    
]





