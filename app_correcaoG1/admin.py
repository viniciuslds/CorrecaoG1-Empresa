from django.contrib import admin
from .models import Pessoa, Funcionario, Departamento, Processo, Documento, PortariaDeInstauracao, Envio, Tramitacoes

@admin.register(Pessoa, Funcionario, Departamento, Processo, Documento, PortariaDeInstauracao, Envio,Tramitacoes)
class AgendaAdmin(admin.ModelAdmin):
    pass
