from django.db import models
from django.contrib.auth.models import User

class Pessoa(models.Model):
    # usuario = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    nome = models.CharField("Nome", max_length=50)
    data_nacimento = models.DateField("Data de Nascimento")

    def __str__(self):
        return self.nome

class Funcionario(Pessoa):
    Matricula = models.CharField('N° de Matricula',  max_length=15)
    Funcao = models.CharField('Função', max_length=20)

    def __str__(self):
        return 'Funcionario ' + self.nome

class Departamento(models.Model):
    nome = models.CharField(verbose_name="Departamento", max_length=50)

    def __str__(self):
        return self.nome

class Processo(models.Model):
    funcionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.SET_NULL)
    dataAbertura = models.DateTimeField(auto_now_add=True)
    local = models.ForeignKey(Departamento, blank=True, null=True, on_delete=models.SET_NULL)
    interessados = models.ManyToManyField(Pessoa, related_name='interessados')
    investigados = models.ManyToManyField(Pessoa, related_name='investigados')

    def __str__(self):
        return 'ok'

class Documento(models.Model):
    processo = models.ForeignKey(Processo, blank=True, null=True, on_delete=models.SET_NULL)
    titulo = models.CharField('Titulo', max_length=15)
    data = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.titulo

class PortariaDeInstauracao(Documento):
    dataMov = models.DateField(auto_now_add=True)
    texto = models.TextField('Breve texto', blank=True, null=True,)


# class Pedido_Prazo(Documento):
#     novoPrazo = models.DateField('Nova Data')
#     antigoPrazo = models.DateField('Antigo Prazo')
#     justificativa = models.TextField('Justificativa')

#     def __str__(self):
#         return self.titulo


class Envio(Documento):
    dataDeEnvio = models.DateField('Data: ', blank=True, null=True)
    departamento = models.ForeignKey(Departamento, blank=True, null=True, on_delete=models.SET_NULL)


class Tramitacoes(models.Model):
    processo = models.ForeignKey(Processo, blank=True, null=True, on_delete=models.SET_NULL)
    origem = models.ForeignKey(Departamento, related_name='origem', blank=True, null=True, on_delete=models.SET_NULL)
    destino = models.ForeignKey(Departamento, blank=True, null=True, on_delete=models.SET_NULL)
    datamov = models.DateField(auto_now_add=True)


