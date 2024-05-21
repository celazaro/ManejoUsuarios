
from django.urls import path
from .views import home, contacto, nosotros, autorizados, cerrar


urlpatterns = [
    
    path('', home, name='home'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    path('autorizados/', autorizados, name='autorizados'),
    path('accounts/logout/', cerrar, name='cerrar'),
    
]