from ..models import Collaborator

def cadastrar_collaborator(collaborator):
    Collaborator.objects.create(first_name = collaborator.first_name,
                                last_name = collaborator.last_name,
                                email = collaborator.email,
                                foto = collaborator.foto,
                                statusAssociacao = collaborator.statusAssociacao)

def listar_collaborators():
    return Collaborator.objects.order_by("id").all()

def listar_colaboradores_nao_associados():
    return Collaborator.objects.filter(statusAssociacao = 0).order_by("id").all()


def listar_collaborator_id(id):
    return Collaborator.objects.get(id=id)

def editar_collaborator(collaborator, collaborator_nova):
    collaborator.first_name = collaborator_nova.first_name
    collaborator.last_name = collaborator_nova.last_name
    collaborator.email = collaborator_nova.email
    collaborator.foto = collaborator_nova.foto
    collaborator.save(force_update=True)

def remover_collaborator(collaborator_bd):
    collaborator_bd.delete()