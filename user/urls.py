from django.urls import path
from user.views import registrar, perfil



urlpatterns = [
    

    path('registrar/', registrar, name='registrar'),
    path('autorizados/perfil/', perfil, name='perfil'),

    
]