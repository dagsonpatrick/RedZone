from django.urls import path
from .views import *

urlpatterns = [

    path('cadastrar_tag/', cadastrar_tag, name='cadastrar_tag'),
    path('listar_tags/', listar_tags, name='listar_tags'),
    path('editar_tag/<int:id>', editar_tag, name='editar_tag'),
    path('remover_tag/<int:id>', remover_tag, name='remover_tag'),


]