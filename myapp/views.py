from django.shortcuts import render, redirect, get_object_or_404
from .forms import VendaForm
from .models import Client, Veiculo, Venda

# Create your views here.

def index(request):
    return render(request, 'index.html')

def listar_veiculos(request):
    veiculos = Veiculo.objects.filter(disponivel=True)
    return render(request, "listar_veiculos.html", {'veiculos': veiculos})

def listar_clientes(request):
    clientes = Client.objects.all()
    return render(request, 'listar_clientes.html', {'clientes': clientes})

def listar_vendas(request):
    vendas = Venda.objects.all()
    return render(request, 'listar_vendas.html', {'vendas': vendas})

def detalhar_veiculo(request, veiculo_id):
    #veiculo = get_object_or_404(Veiculo)
    veiculo = Veiculo.objects.get(id=veiculo_id)
    return render(request, 'detalhar_veiculo.html', {'veiculo': veiculo})

def registrar_venda(request, veiculo_id=None):
    veiculo = None
    dados_iniciais={}
    cliente = None
    venda = None
    
    if veiculo_id:
        veiculo = get_object_or_404(Veiculo, id=veiculo_id)
        dados_iniciais = {'veiculo': veiculo, 'preco': veiculo.preco}

    if request.method == 'POST':
        form = VendaForm(request.POST, initial=dados_iniciais)
        if form.is_valid():
            #cliente = form.cleaned_data['cliente'] Isso já pega do formulário pronto
            #veiculo = form.cleaned_data['veiculo']

            cliente = Client.objects.create(
                name=form.cleaned_data['nome_cliente'],
                email=form.cleaned_data['email_cliente'],
                birth_date = form.cleaned_data['birth_date']
            )
            if veiculo:
                veiculo_disponivel = False
                veiculo.save()
            
            else:
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

        return render(request, 'venda_sucesso.html', {
            'cliente': cliente,
            'veiculo': veiculo,
            'venda': venda
        })
    else:
        form = VendaForm(initial=dados_iniciais)

    return render(request, 'registrar_venda.html', {'form': form, 'veiculo': veiculo})