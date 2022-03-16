from django.db import models
import uuid
from user.models import Account
from .models import *


# Create your models here.


class Admin(models.Model):
    user = models.OneToOneField(Account, on_delete=models.CASCADE)
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    first_name = models.CharField(max_length=25, blank=True, null=True)
    last_name = models.CharField(max_length=25, blank=True, null=True)
    telephone = models.CharField(max_length=25, blank=True, null=True)
    email = models.EmailField(max_length=60, blank=True, null=True)
    add_date  =  models.DateField(auto_now_add=True)
    def __str__(self): 
        return "mr "+self.last_name
