from django.shortcuts import redirect, render
from .forms import FormularioContacto
from django.core.mail import EmailMessage

# Create your views here.

def contacto(request):
    formulario = FormularioContacto
    template_name = 'contacto/contacto.html'

    # captura de elementos del formulario:
    if request.method=='POST':
        formulario = FormularioContacto(data = request.POST)
        # Validamos el contenido del formulario
        if formulario.is_valid():
            nombre = request.POST.get('nombre')         # Capturamos este valor             
            email = request.POST.get('email')           # Capturamos este valor
            contenido = request.POST.get('contenido')   # Capturamos este valor

            # Configuramos el correo de contactacto para nuestro mail:
            email_body = EmailMessage("Mensaje de contacto desde LandingPage",
            "El usuario de {}, desea comunicarse,\n\nha dejado el siguiente mensaje: {}.\nPara dar respuesta escribir un correo a: {}".format(nombre, email, contenido),
            "",["usario@gmail.com"], reply_to=[email])

            try:
                email_body.send()
                # retornamos por get una variable de recibido:
                return redirect('/contacto/?valido')
            except:
                # retornamos por get una variable de recibido:
                return redirect('/contacto/?error')

            

    # agregamos a la funcion render, un diccionario con todos los servicios encontrados:
    return render(request, template_name, {'formulario': formulario});
    