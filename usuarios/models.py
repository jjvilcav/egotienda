from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Usuario(AbstractUser):

    id = models.AutoField(primary_key=True)
    email = models.EmailField(unique=True)
    celular = PhoneNumberField(null=True,blank=True)
    descripcion = models.TextField(max_length=1000,blank=True,null=True)
    foto = models.ImageField(upload_to='profile',blank=True,null=True)

    

    