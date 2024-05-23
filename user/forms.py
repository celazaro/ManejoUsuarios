from django import forms
from django.contrib.auth.forms import UserCreationForm
from user.models import User


class FormularioRegistracion(UserCreationForm):
        first_name = forms.CharField(required=True, label='Nombre')
        last_name = forms.CharField(required=True, label='Apellido')
        email = forms.EmailField(required=True, label='Correo Electrónico')
        class Meta:
             model = User
             fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2' ]

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [ 'username', 'imagen', 'first_name', 'last_name', 'ocupacion', 'direccion', 'localidad',  'provincia', 'pais', 'telefono', 'bio', 'email' ]