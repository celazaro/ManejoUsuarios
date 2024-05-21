from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from user.forms import FormularioRegistracion

# Create your views here.


def registrar (request):
    
    if request.method == 'POST':
        form = FormularioRegistracion (data=request.POST)

        if form.is_valid():

            form.save()

            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password1'] )

            login (request, user)
            return redirect('autorizados')
        
        else:
            return render (request, 'user/registrar.html', {'form':form})
    
    form = FormularioRegistracion 
    return render(request, 'user/registrar.html', {'form':form})


def perfil (request):
    return render (request, 'user/perfil.html')

