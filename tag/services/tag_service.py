from ..models import Tag

def cadastrar_tag(tag):
    Tag.objects.create(description = tag.description,
                       address = tag.address,
                       temperature = tag.temperature,
                       battery = tag.battery,
                       statusAssociacao = tag.statusAssociacao)

def listar_tags():
    return Tag.objects.order_by("id").all()

def listar_tags_nao_associadas():
    return Tag.objects.filter(statusAssociacao = 0).order_by("id").all()

def listar_tag_id(id):
    return Tag.objects.get(id=id)

def listar_tag_address(address):
    return Tag.objects.get(address=address)

def editar_tag(tag, tag_nova):
    tag.description = tag_nova.description
    tag.address = tag_nova.address
    tag.temperature = tag_nova.temperature
    tag.battery = tag_nova.battery
    tag.save(force_update=True)

def remover_tag(tag_bd):
    tag_bd.delete()

