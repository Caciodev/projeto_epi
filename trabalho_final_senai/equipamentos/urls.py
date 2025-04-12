from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro_usuarios/', views.cadastro_usuarios, name='cadastro_usuarios'),
]