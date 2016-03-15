from rest_framework import serializers
from systemservices.contract.models import ContractedService


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContractedService
        fields = ('client', 'service', 'value', 'start', 'end')