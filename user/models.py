from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
        imagen = models.ImageField( default='perfil_default.png', upload_to='users/' )
        ocupacion = models.CharField( max_length=150, null=True, blank=True )
        direccion = models.CharField( max_length=150, null=True, blank=True )
        localidad = models.CharField( max_length=100, null=True, blank=True )
        provincia = models.CharField( max_length=100, null=True, blank=True )
        pais = models.CharField( max_length=100, null=True, blank=True )
        telefono = models.CharField( max_length=100, null=True, blank=True )
        bio = models.TextField( null=True, blank=True )