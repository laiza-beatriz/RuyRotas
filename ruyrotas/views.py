from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InscricaoLinha, Perfil

def index(request):
    return render(request, 'ruyrotas/index.html')

def cad_linhas(request):
    if request.method == 'POST':
        partida = request.POST.get('local_partida')
        chegada = request.POST.get('local_chegada')
        dias = request.POST.get('dias_viagem')
        horario = request.POST.get('horario_linha')
        user = request.user if request.user.is_authenticated else None

        InscricaoLinha.objects.create(usuario=user, local_partida=partida, local_chegada=chegada,
            dias_viagem=dias, horario_linha=horario)

        messages.success(request, 'Inscrição realizada com sucesso!')
        return redirect('cad_linhas')

    return render(request, 'ruyrotas/cad_linhas.html')

def perfil_view(request):
    perfil = Perfil.objects.first()
    return render(request, 'ruyrotas/perfil.html', {'perfil': perfil})
