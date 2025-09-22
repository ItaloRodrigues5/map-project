from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=255, help_text="Nome Completo")
    email = models.EmailField(unique=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.name

class Veiculo(models.Model):
    marca = models.CharField(max_length=255)
    modelo = models.CharField(max_length=255)
    ano = models.IntegerField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f'Marca: {self.marca} - Modelo: {self.modelo} - Ano: {self.ano}'
    
class Venda(models.Model):
    cliente = models.ForeignKey(Client, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data = models.DateField(auto_now_add=True)
    valor_venda = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f'Venda para: {self.cliente} - {self.veiculo}'
    