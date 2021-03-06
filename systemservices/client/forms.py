from django.forms import ModelForm, TextInput, EmailInput
from systemservices.client.models import Client


class ClientModelForm(ModelForm):
    class Meta:
        model = Client
        exclude = ['created_at']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'cpf': TextInput(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'neighborhood': TextInput(attrs={'class': 'form-control'}),
            'number': TextInput(attrs={'class': 'form-control'}),
            'cep': TextInput(attrs={'class': 'form-control'}),
            'city': TextInput(attrs={'class': 'form-control'}),
            'email': EmailInput(attrs={'class': 'form-control'}),
            'phone': TextInput(attrs={'class': 'form-control'}),
        }
