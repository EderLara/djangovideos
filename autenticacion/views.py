from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django import forms
from django.urls import reverse_lazy
from django.contrib import messages
# Paquetes de autenticacion:
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Create your views here.
class VRegistro(CreateView):
    # atributos de la clase VRegsitro:
    form_class = UserCreationForm
    template_name = 'registro/registro.html' 

    # Funcion para agregarle propiedades al formulario de registro:
    def get_form(self, form_class = None):
        form  = super(VRegistro, self).get_form() # Capturamos el formulario de esta vista.
        # Modificación del formulario en tiempo real:
        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb-2', 'required':'true', 'placeholder':'Usuario'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'required':'true', 'placeholder':'Password'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb-2', 'required':'true', 'placeholder':'Confirmar Password'})
        return form

    # Funcion para cuando se obture el boton de enviar:
    def get_success_url(self) -> str:
        return reverse_lazy('ingreso') + '?registro'

# Vista para cerrar sesion:
def cerrar_sesion(request):
    # llamamos la funcion cerrar sesion del framework:
    logout(request)

    return redirect('tienda')

# Vista de Login:
def logear(request):

    template = 'login/login.html'

    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            nickname = form.cleaned_data.get('username')
            userpass = form.cleaned_data.get('password')
            usuario = authenticate(username = nickname, password = userpass)

            if usuario is not None:
                login(request, usuario)
                return redirect('tienda')
            else:
                messages.error(request, 'Usuario y/o Contraseña no válidos')
        
        else:
            messages.error(request, 'Información incorrecta')
        
    form = AuthenticationForm()
    return render(request, 'login/login.html', {'form': form})


