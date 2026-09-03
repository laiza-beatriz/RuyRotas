from django.shortcuts import render

def index(request):
    return render(request, 'ruyrotas/index.html')

def cad_linhas(request):
    return render(request, 'ruyrotas/cad_linhas.html')
