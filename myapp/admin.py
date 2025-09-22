from django.contrib import admin

from .models import Client, Venda, Veiculo

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "birth_date",)
    search_fields = ("name", "email", "birth_date",)
    list_filter = ("name", "email", "birth_date",)

@admin.register(Veiculo)
class VeiculoAdmin(admin.ModelAdmin):
    list_display = ('marca', 'modelo', 'ano', 'preco', 'disponivel')
    search_fields = ('marca', 'modelo', 'ano', 'preco', 'disponivel')
    list_filter = ('marca', 'modelo', 'ano', 'preco', 'disponivel')

@admin.register(Venda)
class VendaAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'veiculo', 'data', 'valor_venda')
    search_fields = ('cliente', 'veiculo', 'data', 'valor_venda')
    list_filter = ('cliente', 'veiculo', 'data', 'valor_venda')