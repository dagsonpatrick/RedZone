from django.shortcuts import render, redirect
from .forms import CollaboratorForm
from .models import Collaborator
from .services import collaborator_service
from django.contrib.auth.decorators import login_required
from PIL import Image
from pathlib import Path
import os
from associar.services import associar_service
from django.contrib import messages

@login_required
def cadastrar_collaborator(request):
    if request.method == "POST":
        form_collaborator = CollaboratorForm(request.POST, request.FILES)
        if form_collaborator.is_valid():
            first_name = form_collaborator.cleaned_data["first_name"]
            last_name = form_collaborator.cleaned_data["last_name"]
            email = form_collaborator.cleaned_data["email"]

            #foto = form_collaborator.cleaned_data["foto"]
            if form_collaborator.cleaned_data["foto"]:
                foto = form_collaborator.cleaned_data["foto"]
            else:
                foto = 'fotoPerfilColaborador/avatar_a4.jpg'

            collaborator_nova = Collaborator(first_name=first_name,
                                             last_name=last_name,
                                             email=email,
                                             foto=foto,
                                             statusAssociacao=0)

            collaborator_service.cadastrar_collaborator(collaborator_nova)
            messages.success(request, str(first_name) +' ' + str(last_name))
            return redirect('listar_collaborators')
    else:
        form_collaborator = CollaboratorForm()
    return render(request, 'collaborator/form_cadastrar_collaborator.html', {'form_collaborator': form_collaborator})

@login_required
def listar_collaborators(request):
    collaborators = collaborator_service.listar_collaborators()
    return render(request, 'collaborator/form_listar_collaborators.html', {'collaborators': collaborators})

@login_required
def editar_collaborator(request, id):
    collaborator = collaborator_service.listar_collaborator_id(id)
    form_collaborator = CollaboratorForm(request.POST, request.FILES)

    if form_collaborator.is_valid():
        first_name = form_collaborator.cleaned_data["first_name"]
        last_name = form_collaborator.cleaned_data["last_name"]
        email = form_collaborator.cleaned_data["email"]

        if form_collaborator.cleaned_data["foto"]:
            foto = form_collaborator.cleaned_data["foto"]
        else:
            foto = collaborator.foto

        collaborator_nova = Collaborator(first_name=first_name,
                                         last_name=last_name,
                                         email=email,
                                         foto=foto)

        collaborator_service.editar_collaborator(collaborator, collaborator_nova)
        messages.info(request, str(first_name) +' ' + str(last_name))
        return redirect('listar_collaborators')
    return render(request, 'collaborator/form_editar_collaborator.html', {'collaborator': collaborator})

@login_required
def remover_collaborator(request, id):

    collaborator_bd = collaborator_service.listar_collaborator_id(id)
    associcao = associar_service.buscar_tag_ass_colaborador(collaborator_bd)

    if associcao is None:
        if request.method == "POST":
            collaborator_service.remover_collaborator(collaborator_bd)
            messages.warning(request, str(collaborator_bd.first_name) + ' ' + str(collaborator_bd.last_name))
            return redirect('listar_collaborators')
        return render(request, 'collaborator/confirma_exclusao.html', {'collaborator':collaborator_bd})
    else:
        collaborator = associcao.collaborator.first_name + ' ' + associcao.collaborator.last_name
        messages.error(request, 'O colaborador ' + collaborator + ' está associado a ' + associcao.tag.description)
        return redirect('listar_collaborators')
