from django import forms
from ejemplo.models import Familiar, Gatos, Perros


class Buscar(forms.Form):
    nombre = forms.CharField(max_length=100,
                             widget= forms.TextInput(attrs={'placeholder': 'Busque algo...'}))

class FamiliarForm(forms.ModelForm):
    class Meta:
        model = Familiar
        fields = ['nombre', 'direccion', 'numero_pasaporte', 'fecha_de_nacimiento']

class GatosForm(forms.ModelForm):
    class Meta:
        model = Gatos
        fields = ['nombre', 'edad', 'sexo']

class PerrosForm(forms.ModelForm):
    class Meta:
        model = Perros
        fields = ['nombre', 'edad', 'sexo']

