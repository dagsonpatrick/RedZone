from ..models import Tag

def cadastrar_tag_automatico(tag):
    tag = Tag.objects.create(uuid=tag.uuid,
                             battery=tag.battery,
                             dateUpdate=tag.date,
                             temperature=22,
                             description='TAG AUTO',
                             statusAssociacao=0,
                             status=0)
    tag.description = 'TAG AUTO ' + tag.id
    tag.save(force_update=True)

def atualizar_tag(tag, battery, dateUpdate):
    tag.battery = battery
    tag.dateUpdate = dateUpdate
    tag.save(force_update=True)

def cadastrar_tag_form(tag):
    Tag.objects.create(description=tag.description,
                       uuid=tag.uuid,
                       statusAssociacao=0)


def listar_tags_gerenciar():
    return Tag.objects.order_by("id").all()

def listar_tags():
    return Tag.objects.filter(status = 1).order_by("id").all()

def listar_tags_nao_associadas():
    return Tag.objects.filter(statusAssociacao=0).filter(status=1).order_by("id").all()

def listar_tag_id(id):
    return Tag.objects.get(id=id)

def buscar_tag_uuid(uuid):
    try:
        return Tag.objects.get(uuid=uuid)
    except Tag.DoesNotExist:
        return False

def editar_tag(tag, tag_nova):
    tag.description = tag_nova.description
    tag.uuid = tag_nova.uuid
    tag.save(force_update=True)

def remover_tag(tag_bd):
    tag_bd.delete()

def ativar_tag_core(id):
    tag = listar_tag_id(id)
    tag.status=1
    tag.save(force_update=True)

def desativar_tag_core(id):
    tag = listar_tag_id(id)
    tag.status=0
    tag.save(force_update=True)


