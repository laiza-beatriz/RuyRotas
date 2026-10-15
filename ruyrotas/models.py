from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    email = models.EmailField(max_length=255, unique=True, verbose_name="E-mail")
    cpf = models.CharField(max_length=11, unique=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

class Perfil(models.Model):
    TIPO_USUARIO = (
        ('ESTUDANTE', 'Estudante'),
        ('MOTORISTA', 'Motorista'),
        ('GESTOR', 'Gestor de Transporte'),
    )

    user = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='perfil')
    tipo = models.CharField(max_length=20, choices=TIPO_USUARIO, default='ESTUDANTE')
    foto = models.ImageField(upload_to='perfis/', blank=True, null=True)
    matricula = models.CharField(max_length=30, blank=True, null=True)
    escola = models.CharField(max_length=120, blank=True, null=True)
    local_partida = models.CharField(max_length=120, blank=True, null=True)
    saida_chegada = models.CharField(max_length=120, blank=True, null=True)

    class Meta:
        permissions = [
            ("pode_gerenciar_linhas", "Pode cadastrar e alterar linhas de transporte"),
        ]

    def __str__(self):
        return f"Perfil de {self.user.get_full_name() or self.user.username}"

class InscricaoLinha(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)
    local_partida = models.CharField(max_length=100)
    local_chegada = models.CharField(max_length=100)
    dias_viagem = models.CharField(max_length=50)
    horario_linha = models.CharField(max_length=10)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.local_partida} ➔ {self.local_chegada} ({self.horario_linha})"

class Cadastro(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    comprovante = models.FileField(upload_to='comprovantes/') 

    def __str__(self):
        return self.nome