from tag.models import Tag
from ..models import AssociacaoCollaborator

def listar_associacoes_colaboradores():
    return AssociacaoCollaborator.objects.all()

def listar_associacao_colaborador_id(id):
    return AssociacaoCollaborator.objects.get(id=id)

def cadastrar_associacao_colaborador(associacao):
    AssociacaoCollaborator.objects.create(tag=associacao.tag,
                                          collaborator_id=associacao.collaborator.id)
    atualiza_statusAssociacao(associacao.collaborator,1)
    atualiza_statusAssociacao(associacao.tag, 1)

def atualiza_statusAssociacao(colaborador, status):
    colaborador.statusAssociacao = status
    colaborador.save(force_update=True)

def remover_associacao_colaborador(associacao):
    associacao.delete()
    atualiza_statusAssociacao(associacao.collaborator, 0)
    atualiza_statusAssociacao(associacao.tag, 0)

def buscar_colaborador_ass_tag(tag):
    try:
        return AssociacaoCollaborator.objects.get(tag_id=tag.id)
    except AssociacaoCollaborator.DoesNotExist:
        return None

def buscar_tag_ass_colaborador(colaborador):
    try:
        return AssociacaoCollaborator.objects.get(collaborator_id=colaborador.id)
    except AssociacaoCollaborator.DoesNotExist:
        return None


def listar_tags():
    return Tag.objects.all()
