from django.urls import path
from user.views import registrar, PerfilView


urlpatterns = [
    

    path('registrar/', registrar, name='registrar'),
    path('autorizados/perfil/', PerfilView.as_view(), name='perfil'),

    
]