from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Client
from .serializers import ClientSerializer

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

# endpoint
class Swagger(APIView):
    def get(self, request):
        return Response({"mensagem": "hello, Swagger!"})