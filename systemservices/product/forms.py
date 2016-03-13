from django.forms import ModelForm, TextInput, NumberInput, Textarea
from systemservices.product.models import Product


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        exclude = ['created_at']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'brand': TextInput(attrs={'class': 'form-control'}),
            'model': TextInput(attrs={'class': 'form-control'}),
            'value': NumberInput(attrs={'class': 'form-control', 'step': 0.25}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'quantity': NumberInput(attrs={'class': 'form-control'}),
        }