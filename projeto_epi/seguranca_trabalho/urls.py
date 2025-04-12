from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro_colaborador, name='cadastro_colaborador'),  # Rota para o formulário de cadastro
    path('sucesso/', views.cadastro_sucesso, name='cadastro_sucesso'),  # Página de sucesso
    path('colaboradores/', views.lista_colaboradores, name='lista_colaboradores'),  # Lista de colaboradores
]
