from rest_framework import serializers
from myapp.models import Client, Veiculo, Venda

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '_all_'
        extra_kwargs = {
            'nome': {'help_text': 'Nome completo do cliente'},
            'email': {'help_text': 'Email válido do cliente'}
        }
    def validate_email(self, value):
        if not value.endswith('gmail.com'):
            raise serializers.ValidationError("O email precisa ser do Gmail")
        return value
class VeiculoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Veiculo
        fields = '_all_'

class VendaSerializer(serializers.ModelSerializer):
    cliente = ClientSerializer()
    veiculo = VeiculoSerializer()
    
    class Meta:
        model = Venda
        fields = '_all_'