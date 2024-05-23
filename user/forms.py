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
             
        #Este código permite verificar que el correo no se repita en varios usuarios.
        def clean_email(self):
            email = self.cleaned_data['email']

            if User.objects.filter(email=email).exists():
                raise forms.ValidationError('Este correo electrónico ya está registrado!!')
            return email

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = [ 'username', 'imagen', 'first_name', 'last_name', 'ocupacion', 'direccion', 'localidad',  'provincia', 'pais', 'telefono', 'bio', 'email' ]