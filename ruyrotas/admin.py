from django.contrib import admin
from .models import InscricaoLinha, Perfil

class InscricaoLinhaAdmin(admin.ModelAdmin):
    list_display = ('local_partida', 'local_chegada', 'dias_viagem', 'horario_linha', 'data_cadastro')

admin.site.register(InscricaoLinha, InscricaoLinhaAdmin)

@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'matricula', 'escola', 'local_partida')
    search_fields = ('user__username', 'matricula')
