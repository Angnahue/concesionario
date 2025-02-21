from django import forms
from .models import Cliente, ModeloDeAuto, Vendedor

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'email', 'telefono']

class ModeloDeAutoForm(forms.ModelForm):
    class Meta:
        model = ModeloDeAuto
        fields = ['marca', 'modelo', 'anio']

class VendedorForm(forms.ModelForm):
    class Meta:
        model = Vendedor
        fields = ['nombre', 'email', 'telefono']

class BuscarModeloForm(forms.Form):
    consulta = forms.CharField(label='Buscar modelo', max_length=100)
