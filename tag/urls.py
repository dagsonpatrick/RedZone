from django.urls import path
from .views import listar_tags, cadastrar_tag, editar_tag, gerenciar_tags, ativar_tag, desativar_tag, remover_tag

urlpatterns = [

    path('cadastrar_tag/', cadastrar_tag, name='cadastrar_tag'),
    path('listar_tags/', listar_tags, name='listar_tags'),
    path('editar_tag/<int:id>', editar_tag, name='editar_tag'),
    path('remover_tag/<int:id>', remover_tag, name='remover_tag'),

    path('gerenciar_tags/', gerenciar_tags, name='gerenciar_tags'),
    path('ativar_tag/<int:id>', ativar_tag, name='ativar_tag'),
    path('desativar_tag/<int:id>', desativar_tag, name='desativar_tag'),

]