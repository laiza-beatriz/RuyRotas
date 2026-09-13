from django.db import models
from django.contrib.auth.models import User

class InscricaoLinha(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    local_partida = models.CharField(max_length=100)
    local_chegada = models.CharField(max_length=100)
    dias_viagem = models.CharField(max_length=50)
    horario_linha = models.CharField(max_length=10)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.local_partida} ➔ {self.local_chegada} ({self.horario_linha})"

class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True)
    matricula = models.CharField(max_length=30)
    escola = models.CharField(max_length=120)
    local_partida = models.CharField(max_length=120)
    saida_chegada = models.CharField(max_length=120)

    def __str__(self):
        return f"Perfil de {self.user.username}"