from django import forms
from .models import Cliente, Premio, Ganador, Configuracion

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['numero_documento', 'nombre', 'apellidos', 'numero_celular', 'numero_factura']
        widgets = {
            'numero_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellidos': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_celular': forms.TextInput(attrs={'class': 'form-control'}),
            'numero_factura': forms.TextInput(attrs={'class': 'form-control'}),
            }
        
class PremioForm(forms.ModelForm):
    class Meta:
        model = Premio
        fields = ['nombre', 'descripcion', 'probabilidad']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
            'probabilidad': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

class GanadorForm(forms.ModelForm):
    class Meta:
        model = Ganador
        fields = ['cliente', 'premio']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-control'}),
            'premio': forms.Select(attrs={'class': 'form-control'}),
            }
class ConfiguracionForm(forms.ModelForm):
    class Meta:
        model = Configuracion
        fields = ['probabilidad_no_ganar']
        widgets = {
            'probabilidad_no_ganar': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }

