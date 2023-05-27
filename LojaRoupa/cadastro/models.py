from django.db import models

# Create your models here.
class Cliente(models.Model):
    id_cliente = 0 ##descobrir como gerar ir auto incremento##
    nome = models.CharField(max_length=28, verbose_name="Nome")
    cpf = models.CharField(max_length=11, verbose_name="CPF")
    rg = models.CharField(max_length=10, verbose_name="RG")
    data_de_nascimento = models.DateField(verbose_name="Data de Nascimento")
    telefone = models.CharField(max_length=11, verbose_name="Celular")
    endereco = models.CharField(max_length=255, verbose_name="Endereço")

    def __str__(self):
        return self.id_cliente


class Locacao(models.Model):
	id_locacao = 0 ##descobrir como gerar id auto incremento##
	dataContratacao = models.DateField()
	dataLocacao = models.DateField()
    #cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
def __str__(self):
        return self.id_locacao


class ContaReceber(models.Model):
    id_recebimento = 0 ##descobrir como gerar id auto incremento##
    #id_locacao = models.ForeignKey(Locacao, on_delete=models.PROTECT) Precisa criar locacao e client antes.
    #id_cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
    data_recebimento =  models.DateField()
    valor_recebimento = models.DecimalField(max_digits = 8, decimal_places=2)  

    def __str__(self):
        return self.id_recebimento
