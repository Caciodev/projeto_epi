from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'seguranca_trabalho/home.html')