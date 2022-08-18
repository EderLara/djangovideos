from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(label='Nombre', widget=forms.TextInput(attrs={'class':'form-control'}), required=True)
    email = forms.EmailField(label='Correo Electrónico', widget=forms.EmailInput(attrs={'class':'form-control'}), required=True)
    contenido = forms.CharField(label = "Mensaje", widget=forms.Textarea(attrs={'class':'form-control', 'rows':'4'}), required=True)