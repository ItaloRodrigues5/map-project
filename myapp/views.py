from django.shortcuts import render, redirect, get_object_or_404
from .forms import VendaForm
from .models import Client, Veiculo, Venda

# Create your views here.

def listar_veiculos(request):
    veiculos = Veiculo.objects.filter(disponivel=True)
    return render(request, "listar_veiculos.html", {'veiculos': veiculos})

def listar_clientes(request):
    clientes = Client.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'listar_vendas.html', {'vendas': vendas})

def registrar_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            #cliente = form.cleaned_data['cliente'] Isso já pega do formulário pronto
            #veiculo = form.cleaned_data['veiculo']

            cliente = Client.objects.create(
                name=form.cleaned_data['nome_cliente'],
                email=form.cleaned_data['email_cliente'],
                birth_date = form.cleaned_data['birth_date']
            )

            veiculo = Veiculo.objects.create(
                marca=form.cleaned_data['marca_veiculo'],
                modelo=form.cleaned_data['modelo_veiculo'],
                ano=form.cleaned_data['ano_veiculo'],
                preco=form.cleaned_data['preco_veiculo']
            )

            venda = Venda.objects.create(
            cliente = cliente,
            veiculo = veiculo,
            valor_venda = veiculo.preco
        )
        veiculo_disponivel = False
        veiculo.save()

        return render(request, 'venda_sucesso.html', {
            'cliente': cliente,
            'veiculo': veiculo,
            'venda': venda
        })
    else:
        form = VendaForm()

    return render(request, 'registrar_venda.html', {'form': form})