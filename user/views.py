from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from user.forms import FormularioRegistracion, UserForm
from django.views.generic import TemplateView

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


# PAGINA DE PERFIL
class PerfilView(TemplateView):
    template_name = 'user/perfil.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context['user_form'] = UserForm(instance=user)

        return context

    def post(self, request, *args, **kwargs):
        user = self.request.user
        user_form = UserForm(request.POST, request.FILES, instance=user)

        if  user_form.is_valid():   
            user_form.save()
            # Redireccionar a la pagina de perfil (con datos actualizados)
            return redirect('perfil')

        # Si alguno de los datos no es valido
        context = self.get_context_data()
        context['user_form'] = user_form
        
        return render(request, 'user/perfil.html', context)
    
