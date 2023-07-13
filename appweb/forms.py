from django import forms
from .models import *

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = "__all__"

class ProfesionalForm(forms.ModelForm):

    class Meta:
        model = Profesional
        fields = "__all__"

widgets = {
            "fecha_nacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
        }

class AtencionForm(forms.ModelForm):
    
    class Meta:
        model = Atencion
        exclude = ['mecanico', 'estado', 'motivoRechazo']


class MotivoRechazoForm(forms.ModelForm):
    motivo_rechazo = forms.CharField(max_length=100, widget=forms.Textarea)

class TrabajaConNosotrosForm(forms.ModelForm):
    foto = forms.ImageField(required=False)
    class Meta:
        model = TrabajaConNosotros    
        fields = "__all__"
        widgets = {
                    "fechaNacimiento" : forms.DateInput(attrs={'type': 'date'}, format=('%Y-%m-%d'))
                }