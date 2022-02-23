from operator import mod
from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200, verbose_name="Nombre", null=False, blank=False)
    last_name = models.CharField(max_length=200, verbose_name="Apellido", null=False, blank=False)
    username = models.CharField(max_length=50, verbose_name="Usuario", null=False, blank=False, unique=True)
    email = models.EmailField(max_length=254, null=False, blank=False, unique= True)
