from django import forms
from .models import Client, Veiculo

class VendaForm(forms.Form):
    #cliente = forms.ModelChoiceField(queryset=Client.objects.all(), label='Cliente') #Select Option HTML

    nome_cliente = forms.CharField(label='Nome do Cliente', max_length=255)
    email_cliente = forms.CharField(label='E-mail do Cliente')
    birth_date = forms.DateField(label='Data de Nascimento', widget=forms.DateInput(attrs={'type': 'date'}))
        
    veiculo = forms.ModelChoiceField(queryset=Veiculo.objects.filter(disponivel=True), label='Veículo')

    marca_veiculo = forms.CharField(label='Marca do Veículo', max_length=50)
    modelo_veiculo = forms.CharField(label='Modelo do Veículo', max_length=50)
    ano_veiculo = forms.IntegerField(label="Ano do Veículo")
    preco_veiculo = forms.DecimalField(label='Preço do Veículo', max_digits=10, decimal_places=2)