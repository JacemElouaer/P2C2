from django.urls import path
from .views import *


urlpatterns = [
    #manager  urls
    path('create_pc/', create_PCCollection , name="create_PCCollection"),
    path('get_by_manager_id/', get_pc_by_manager_id, name="get_pc_by_manager_id"),
    path('get_pc_id/', get_pc_by_id, name="get_pc_by_id"),
    path('vendor' ,  index_pc ,  name="index_pc")
    

]
