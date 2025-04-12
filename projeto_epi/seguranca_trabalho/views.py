from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'seguranca_trabalho/home.html')

from django.shortcuts import render, redirect
from .models import Colaborador

def cadastro_colaborador(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        idade = request.POST.get('idade')
        email = request.POST.get('email')
        telefone = request.POST.get('telefone')
        cargo = request.POST.get('cargo')

        # Salva os dados no banco
        colaborador = Colaborador(
            nome=nome,
            idade=idade,
            email=email,
            telefone=telefone,
            cargo=cargo
        )
        colaborador.save()

        return redirect('cadastro_sucesso')  # Redireciona para uma página de sucesso

    return render(request, 'cadastro/colaborador_form.html')

def cadastro_sucesso(request):
    return render(request, 'cadastro/sucesso.html')

def lista_colaboradores(request):
    colaboradores = Colaborador.objects.all()  # Busca todos os colaboradores
    return render(request, 'cadastro/lista_colaboradores.html', {'colaboradores': colaboradores})