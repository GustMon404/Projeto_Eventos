from django.contrib import admin
from .models import Pessoa,PessoaFisica,Ingresso, Inscricao, Evento

@admin.register(Pessoa,PessoaFisica,Ingresso, Inscricao, Evento)

class EventoAdmin(admin.ModelAdmin):
    pass
# Register your models here.