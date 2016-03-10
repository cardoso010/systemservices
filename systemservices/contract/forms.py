from django.forms import ModelForm, Select, NumberInput, SelectDateWidget
from systemservices.contract.models import ContractedService


class ContractModelForm(ModelForm):
    class Meta:
        model = ContractedService
        fields = '__all__'
        widgets = {
            'client': Select(attrs={'class': 'form-control'}),
            'service': Select(attrs={'class': 'form-control'}),
            'value': NumberInput(attrs={'class': 'form-control', 'step': 0.25}),
            'start': SelectDateWidget(attrs={'class': 'form-control'}),
            'end': SelectDateWidget(attrs={'class': 'form-control'}),
        }