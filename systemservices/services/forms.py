from django.forms import ModelForm, TextInput, NumberInput
from systemservices.services.models import Service


class ServiceModelForm(ModelForm):
    class Meta:
        model = Service
        exclude = ['created_at']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'value': NumberInput(attrs={'class': 'form-control', 'step': 0.25}),
        }