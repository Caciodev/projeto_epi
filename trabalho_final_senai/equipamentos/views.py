from django.shortcuts import render

# Create your views here.
def cadastro_usuarios(request):
    return render(request, 'cadastro_usuarios.html')
