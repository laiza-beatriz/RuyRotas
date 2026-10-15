from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required, permission_required
from .models import InscricaoLinha, Perfil, Usuario, Cadastro
from .forms import PerfilForm


def index(request):
    return render(request, 'ruyrotas/index.html')

@login_required
def linhas(request):
    user = request.user
    linha_usuario = None

    if hasattr(user, 'linha'):
        linha_usuario = user.linha
    elif hasattr(user, 'perfil') and hasattr(user.perfil, 'linha'):
        linha_usuario = user.perfil.linha

    return render(request, 'ruyrotas/linhas.html', {
        'linha': linha_usuario
    })

@login_required
def cad_linhas(request):
    if request.method == 'POST':
        partida = request.POST.get('local_partida')
        chegada = request.POST.get('local_chegada')
        dias = request.POST.get('dias_viagem')
        horario = request.POST.get('horario_linha')

        InscricaoLinha.objects.create(
            usuario=request.user,
            local_partida=partida,
            local_chegada=chegada,
            dias_viagem=dias,
            horario_linha=horario
        )

        messages.success(request, 'Inscrição realizada com sucesso!')
        return redirect('cad_linhas')

    return render(request, 'ruyrotas/cad_linhas.html')


@login_required
def perfil_view(request):
    perfil, created = Perfil.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        perfil.escola = request.POST.get('escola', perfil.escola)
        perfil.matricula = request.POST.get('matricula', perfil.matricula)
        perfil.local_partida = request.POST.get('local_partida', perfil.local_partida)
        perfil.saida_chegada = request.POST.get('saida_chegada', perfil.saida_chegada)
        if request.FILES.get('foto'):
            perfil.foto = request.FILES.get('foto')
        perfil.save()
        messages.success(request, 'Perfil atualizado com sucesso!')
        return redirect('perfil')

    return render(request, 'ruyrotas/perfil.html', {'perfil': perfil})


def cadastro(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmacao_senha = request.POST.get('confirmacao_senha')
        comprovante = request.FILES.get('comprovante')

        if senha != confirmacao_senha:
            messages.error(request, 'As senhas não coincidem.')
            return render(request, 'ruyrotas/cadastro.html')

        if Usuario.objects.filter(email=email).exists():
            messages.error(request, 'Este e-mail já está cadastrado.')
            return render(request, 'ruyrotas/cadastro.html')

        usuario = Usuario.objects.create_user(
            username=email,
            email=email,
            password=senha,
            first_name=nome
        )

        if comprovante:
            Cadastro.objects.create(nome=nome, email=email, comprovante=comprovante)

        Perfil.objects.get_or_create(user=usuario)

        return redirect('linhas')
       
        login(request, usuario)
        messages.success(request, 'Cadastro realizado com sucesso!')
        return redirect('index')

    return render(request, 'ruyrotas/cadastro.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        usuario = authenticate(request, username=email, password=senha)

        if usuario is not None:
            login(request, usuario)
            return redirect('index')
        else:
            messages.error(request, 'E-mail ou senha incorretos.')

    return render(request, 'ruyrotas/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)
    return render(request, "ruyrotas/perfil.html", {"perfil": perfil})


@login_required
def editar_perfil(request):
    perfil, _ = Perfil.objects.get_or_create(user=request.user)

    if request.method == "POST":
        form = PerfilForm(request.POST, request.FILES, instance=perfil, user=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Perfil atualizado com sucesso!")
            return redirect("perfil")
    else:
        form = PerfilForm(instance=perfil, user=request.user)

    return render(request, "ruyrotas/editar_perfil.html", {"form": form, "perfil": perfil})
    return render(request, "ruyrotas/editar_perfil.html", {"form": form, "perfil": perfil})