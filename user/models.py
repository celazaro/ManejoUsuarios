from django.db import models
from django.contrib.auth.models import AbstractUser

import os

from django.conf import settings
from django.core.files.storage import default_storage

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

        def save(self, *args, **kwargs):
        # Verificar que la imagen que estoy subiendo es diferente a la predeterminada
                if self.pk and self.imagen.name != 'perfil_default.png':
                        viejo_perfil = User.objects.get(pk=self.pk)
                        default_imagen_path = os.path.join(settings.MEDIA_ROOT, 'perfil_default.png')
                
                        if viejo_perfil.imagen.path != self.imagen.path and viejo_perfil.imagen.path != default_imagen_path:
                                # Voy a eliminar la imagen anteniro si es distinta de la actual y distinta de perfil_default.png
                                default_storage.delete(viejo_perfil.imagen.path)
                
                super(User, self).save(*args, **kwargs)
    