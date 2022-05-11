from ..models import Register
from collaborator.services import collaborator_service


def insert_register(evento):
    Register.objects.create(portal=evento.portal,
                            tag=evento.tag,
                            collaborator=evento.collaborator,
                            sentido=evento.sentido,
                            temperature=evento.temperature,
                            battery= evento.battery,
                            timestamp=evento.timestamp)


def register_timeline_collaborator(dtInicial, dtFinal, collaborator_id):
    collaborator = collaborator_service.listar_collaborator_id(collaborator_id)
    registers = Register.objects.filter(collaborator=collaborator, timestamp__range=[dtInicial, dtFinal]).order_by("timestamp")
    return registers


def listar_register():
    registers = Register.objects.order_by("-timestamp")[:10]
    return registers


def events_register(dtInicial, dtFinal):
    registers = Register.objects.filter(timestamp__range=[dtInicial, dtFinal])
    return registers

def normalizer_register_export_excel(registros):
    registers = []
    for r in registros:
        registers.append([r.collaborator.first_name +' '+ r.collaborator.last_name, r.sentido, r.tag.description, r.battery, r.temperature, r.timestamp])
    return registers