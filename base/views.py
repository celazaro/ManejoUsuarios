from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.

def home(request):
    return render (request, 'base/inicio.html')

def contacto(request):
    return render (request, 'base/contacto.html')

def nosotros(request):
    return render (request, 'base/nosotros.html')

def cerrar (request):
    logout (request)
    return redirect ('/')

@login_required
def autorizados (request):
    return render (request, 'base/autorizados.html')