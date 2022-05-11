from django.urls import path
from .views import cadastrar_collaborator, listar_collaborators, editar_collaborator, remover_collaborator

urlpatterns = [

    path('cadastrar_collaborator/', cadastrar_collaborator, name='cadastrar_collaborator'),
    path('listar_collaborator/', listar_collaborators, name='listar_collaborators'),
    path('editar_collaborator/<int:id>', editar_collaborator, name='editar_collaborator'),
    path('remover_collaborator/<int:id>', remover_collaborator, name='remover_collaborator'),

]