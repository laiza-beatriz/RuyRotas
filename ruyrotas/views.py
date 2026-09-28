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

def cadastro(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        comprovante = request.FILES.get('comprovante') 
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('confirmacao_senha')

        if senha != confirmacao_senha:
            messages.error(request, 'As palavras-passes não coincidem.')
            return render(request, 'cadastro.html')
        
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('login')

    return render(request, 'ruyrotas/cadastro.html')

def login_view(request):
    if request.method == 'POST':
        return redirect('home')
        
    return render(request, 'ruyrotas/login.html')