from django.urls import path
from .views import *

urlpatterns = [

    path('associar_colaborador/', associar_colaborador, name='associar_colaborador'),
    path('listar_associacoes_colaboradores/', listar_associacoes_colaboradores, name='listar_associacoes_colaboradores'),
    path('remover_associacao_colaborador/<int:id>', remover_associacao_colaborador, name='remover_associacao_colaborador'),

    path('exibir_associacoes/', exibir_associacoes, name='exibir_associacoes'),
    path('listar_associacoes/', listar_associacoes, name='listar_associacoes'),

]