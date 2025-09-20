from rest_framework import serializers
from myapp.models import Client
from myapp.models import Veiculo
from myapp.models import Venda

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '_all_'

class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '_all_'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '_all_'