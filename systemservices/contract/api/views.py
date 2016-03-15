from rest_framework.decorators import api_view
from rest_framework.response import Response
from systemservices.contract.models import ContractedService
from systemservices.contract.api.serializers import ContractSerializer


@api_view(['GET'])
def api_list(request):
    if request.method == 'GET':
        contract = ContractedService.objects.all()
        serializer = ContractSerializer(contract, many=True)
        return Response(serializer.data)

