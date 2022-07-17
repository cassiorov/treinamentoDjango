from django.urls import path
from . import views


urlpatterns = [
    path('cadastro/', views.cadastro, name='cadastro'),
    path('listar', views.listar, name='listar'),
    path('listar/<int:id_pessoa>', views.listar_unico, name='listar_unico')  # url dinâmica
]
