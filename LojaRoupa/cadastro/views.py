from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from .models import Cliente, Locacao, ContaReceber
from django.urls import reverse_lazy

# Create your views here.

class CreateCliente(CreateView):
    model = Cliente
    fields = [
        'nome', 
        'cpf', 
        'rg',
        'data_de_nascimento', 
        'telefone',
        'endereco',
        ]
    template_name = 'cadastro/cadastro.html'
    success_url = reverse_lazy('listar-cliente')

class CreateLocacao(CreateView):
    model = Locacao
    fields = [
        'nome_cliente',
        'data_contratacao',
        'data_locacao',
        ]
    template_name = 'cadastro/cadastro.html'
    success_url = reverse_lazy('listar-locacao')

class CreateContaReceber(CreateView):
    model = ContaReceber
    fields = [
        'id_recebimento',
        'id_locacao',
        'nome_cliente',
        'data_recebimento',
        'valor_recebimento',
        ]
    template_name = 'cadastro/cadastro.html'      
    success_url = reverse_lazy('listar-contareceber')
    

############ UPDATE  ############

class UpdateCliente(UpdateView):
    model = Cliente
    fields = [
        'id_cliente',
        'nome', 
        'cpf', 
        'rg',
        'data_de_nascimento', 
        'telefone',
        'endereco',
        ]
    template_name = 'cadastro/cadastro.html'
    success_url = reverse_lazy('listar-cliente')

class UpdateLocacao(UpdateView):
    model = Locacao
    fields = [
        'nome_cliente',
        'data_contratacao',
        'data_locacao',
        ]
    template_name = 'cadastro/cadastro.html'
    success_url = reverse_lazy('listar-locacao')

class UpdateContaReceber(UpdateView):
    model = ContaReceber
    fields = [
        'id_recebimento',
        'id_locacao',
        'nome_cliente',
        'data_recebimento',
        'valor_recebimento',
        ]
    template_name = 'cadastro/cadastro.html'
    success_url = reverse_lazy('listar-contareceber')
    

#### DELETE VIEW ####

class DeleteCliente(DeleteView):
    model = Cliente
    template_name = 'cadastro/cadastro-excluir.html'
    success_url = reverse_lazy('listar-cliente')

class DeleteLocacao(DeleteView):
    model = Locacao
    template_name = 'cadastro/cadastro-excluir.html'
    success_url = reverse_lazy('listar-locacao')

class DeleteContaReceber(DeleteView):
    model = ContaReceber
    template_name = 'cadastro/cadastro-excluir.html'
    success_url = reverse_lazy('listar-contareceber')

### LIST VIEW ####

class ViewCliente(ListView):
    model = Cliente
    template_name = 'cadastro/consultar/cliente.html'


class ViewLocacao(ListView):
    model = Locacao
    template_name = 'cadastro/consultar/locacao.html'


class ViewContaReceber(ListView):
    model = ContaReceber
    template_name = 'cadastro/consultar/conta_receber.html'
    