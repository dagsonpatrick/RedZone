from django.shortcuts import render, redirect
from .forms import TagForm
from .models import Tag
from .services import tag_service
from django.contrib.auth.decorators import login_required
from associar.services import associar_service
from django.contrib import messages


@login_required()
def cadastrar_tag(request):
    if request.method == "POST":
        form_tag = TagForm(request.POST)
        if form_tag.is_valid():
            description = form_tag.cleaned_data["description"]
            address = form_tag.cleaned_data["address"]
            temperature = form_tag.cleaned_data["temperature"]
            battery = form_tag.cleaned_data["battery"]

            tag_nova = Tag(description=description,
                                 address=address,
                                 temperature=temperature,
                                 battery=battery,
                                statusAssociacao = 0
                           )

            tag_service.cadastrar_tag(tag_nova)
            return redirect('listar_tags')
    else:
        form_tag = TagForm()
    return render(request, 'tag/form_cadastrar_tag.html', {'form_tag': form_tag})

@login_required()
def listar_tags(request):
    tags = tag_service.listar_tags()
    return render(request, 'tag/form_listar_tags.html', {'tags': tags})

@login_required()
def editar_tag(request, id):
    tag = tag_service.listar_tag_id(id)
    form_tag = TagForm(request.POST)

    if form_tag.is_valid():
        description = form_tag.cleaned_data["description"]
        address = form_tag.cleaned_data["address"]
        temperature = form_tag.cleaned_data["temperature"]
        battery = form_tag.cleaned_data["battery"]

        tag_nova = Tag(description=description,
                      address=address,
                      temperature=temperature,
                      battery=battery)
        tag_service.editar_tag(tag, tag_nova)
        return redirect('listar_tags')
    return render(request, 'tag/form_editar_tag.html', {'tag': tag})

@login_required()
def remover_tag(request, id):

    tag_bd = tag_service.listar_tag_id(id)
    associcao = associar_service.buscar_colaborador_ass_tag(tag_bd)

    if associcao is None:
        if request.method == "POST":
            tag_service.remover_tag(tag_bd)
            return redirect('listar_tags')
        return render(request, 'tag/confirma_exclusao.html', {'tag':tag_bd})
    else:
        collaborator = associcao.collaborator.first_name + ' ' +associcao.collaborator.last_name
        messages.error(request, tag_bd.description + ' está associada ao colaborador: ' + collaborator)
        return redirect('listar_tags')

