from django.urls import path
from .views import CreateCliente, CreateLocacao, CreateContaReceber
from .views import UpdateCliente, UpdateLocacao, UpdateContaReceber
from .views import DeleteCliente, DeleteLocacao, DeleteContaReceber
from .views import ViewCliente, ViewLocacao, ViewContaReceber
urlpatterns =[
    path('cadastro/cliente/', CreateCliente.as_view(), name='cadastro-cliente'),
    path('cadastro/locacao/', CreateLocacao.as_view(), name='cadastro-locacao'),
    path('cadastro/conta_receber/', CreateContaReceber.as_view(), name='cadastro-contareceber'),

    #### URLs UPDATE ####
    path('editar/cliente/<int:pk>/', UpdateCliente.as_view(), name='editar-cliente'),
    path('editar/locacao/<int:pk>/', UpdateLocacao.as_view(), name='editar-locacao'),
    path('editar/conta_receber/<int:pk>/', UpdateContaReceber.as_view(), name='editar-contareceber'),

    #### URLs DELETE ####
    path('excluir/cliente/<int:pk>', DeleteCliente.as_view(), name='excluir-cliente' ),
    path('excluir/locacao/<int:pk>', DeleteLocacao.as_view(), name='excluir-locacao' ),
    path('excluir/conta_receber/<int:pk>', DeleteContaReceber.as_view(), name='excluir-contareceber'),

    #### URLs ListView #### 
    path('consultar/cliente', ViewCliente.as_view(), name='listar-cliente'),
    path('consultar/locacao', ViewLocacao.as_view(), name='listar-locacao'),
    path('consultar/conta_receber', ViewContaReceber.as_view(), name='listar-contareceber'),
]