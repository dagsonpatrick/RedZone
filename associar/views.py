from django.shortcuts import render, redirect

from .forms import ColaboradorForm
from .entidades.associarCollaborator import AssociarCollaborator
from .services import associar_service
from collaborator.services import collaborator_service
from tag.services import tag_service
from api.services import evento_service
from django.contrib.auth.decorators import login_required

@login_required
def associar_colaborador(request):
    lista_colaboradores = collaborator_service.listar_colaboradores_nao_associados()
    lista_tag = tag_service.listar_tags_nao_associadas()
    associacoes = associar_service.listar_associacoes_colaboradores()

    if request.method == "POST":
        form_associacao = ColaboradorForm(request.POST)
        if form_associacao.is_valid():
            tag = form_associacao.cleaned_data["tag"]
            collaborator = form_associacao.cleaned_data["collaborator"]
            associacao_nova = AssociarCollaborator(tag=tag,
                                 collaborator=collaborator)
            associar_service.cadastrar_associacao_colaborador(associacao_nova)
            return render(request, 'associacao/form_cadastrar_associacao_colaborador.html', { 'associacoes': associacoes, 'lista_tag':lista_tag, 'lista_colaboradores':lista_colaboradores, 'form_associacao': form_associacao})
    else:
        form_associacao = ColaboradorForm()
    return render(request, 'associacao/form_cadastrar_associacao_colaborador.html', { 'associacoes': associacoes, 'lista_tag':lista_tag, 'lista_colaboradores':lista_colaboradores, 'form_associacao': form_associacao})

@login_required
def listar_associacoes_colaboradores(request):
    associacoes = associar_service.listar_associacoes_colaboradores()
    return render(request, 'associacao/form_listar_associacoes_colaboradores.html', {'associacoes': associacoes})

@login_required
def remover_associacao_colaborador(request, id):
    associacao_bd = associar_service.listar_associacao_colaborador_id(id)
    if request.method == "POST":
        associar_service.remover_associacao_colaborador(associacao_bd)
        evento_service.remove_evento_redzone(associacao_bd.collaborator)
        return redirect('associar_colaborador')
    return render(request, 'associacao/confirma_exclusao_ass_colaborador.html', {'associacao':associacao_bd})

@login_required
def exibir_associacoes(request):
    return render(request, 'associacao/form_exibir_associacao.html',{})

@login_required
def listar_associacoes(request):
    if request.method == "POST":
        associacao = request.POST.get("associacao")
        if associacao == "Colaboradores":
            return redirect(listar_associacoes_colaboradores)


