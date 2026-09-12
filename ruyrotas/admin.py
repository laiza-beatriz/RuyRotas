from django.contrib import admin
from .models import InscricaoLinha

class InscricaoLinhaAdmin(admin.ModelAdmin):
    list_display = ('local_partida', 'local_chegada', 'dias_viagem', 'horario_linha', 'data_cadastro')

admin.site.register(InscricaoLinha, InscricaoLinhaAdmin)
