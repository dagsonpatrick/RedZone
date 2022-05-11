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