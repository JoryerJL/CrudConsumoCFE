from django import forms
from .models import State, Municipality, PostalCode, Colony, Client

class ClientForm(forms.ModelForm):
    name = forms.CharField(label="Nombre", help_text="Escribe tu nombre", max_length=100, required=True)
    paternal_surname = forms.CharField(label="Apellido Paterno", help_text="Escribe tu apellido paterno",max_length=100, required=True)
    maternal_surname = forms.CharField(label="Apellido Materno", help_text="Escribe tu apellido materno",max_length=100, required=True)
    phone_number = forms.IntegerField(label="Número de teléfono", help_text="Escribe tu número de teléfono", max_value=9999999999, min_value=1000000000, required=True)
    street = forms.CharField(label="Calle", help_text="Escribe tu calle",max_length=100, required=True)
    interior_number = forms.CharField(label="Número interior", help_text="Escribe tu número interior", required=False)
    external_number = forms.CharField(label="Número exterior", help_text="Escribe tu número exterior", required=False)

    class Meta:
        model = Client
        fields = ['name', 'paternal_surname', 'maternal_surname', 'phone_number', 'street', 'interior_number', 'external_number', 'colony']
        labels = {
            'colony': 'Colonia',
        }

class StateForm(forms.ModelForm):
    name = forms.CharField(label="Nombre", help_text="Escribe el nombre del estado", max_length=100, required=True)
    class Meta:
        model = State
        fields = ['name']

class ColonyForm(forms.ModelForm):
    name = forms.CharField(label="Nombre", help_text="Escribe el nombre de la colonia", max_length=100, required=True)
    class Meta:
        model = Colony
        fields = ['name', 'postal_code']
        labels = {
            'postal_code': 'Código postal'
        }

class PostalCodeForm(forms.ModelForm):
    postal_code = forms.IntegerField(label="Código postal", help_text="Escribe el código postal", required=True)
    class Meta:
        model = PostalCode
        fields = ['postal_code', 'municipality']
        labels = {
            'municipality': 'Municipio'
        }

class MunicipalityForm(forms.ModelForm):
    name = forms.CharField(label="Nombre", help_text="Escribe el nombre del municipio", max_length=100, required=True)
    class Meta:
        model = Municipality
        fields = ['name', 'state']
        labels = {
            'state': 'Estado'
        }