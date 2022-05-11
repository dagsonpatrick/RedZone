from ..models import EventoRedZone, EventoCore
from register.services import register_service

def cadastrar_evento(evento):

    try:
         EventoRedZone.objects.get(status=evento.status, tag=evento.tag)

    except EventoRedZone.DoesNotExist:
        if evento.status == 1:
            try:
                event_in_old = EventoRedZone.objects.get(status=0, tag=evento.tag)
                atualizar_evento(event_in_old, evento, 1)
                register_service.insert_register(evento)
            except EventoRedZone.DoesNotExist:
                EventoRedZone.objects.create(portal = evento.portal,
                                             tag = evento.tag,
                                             collaborator = evento.collaborator,
                                             sentido = evento.sentido,
                                             temperature = evento.temperature,
                                             battery =  evento.battery,
                                             status = evento.status,
                                             timestamp = evento.timestamp)
                register_service.insert_register(evento)
        else:
            try:
                event_out_old = EventoRedZone.objects.get(status=1, tag=evento.tag)
                atualizar_evento(event_out_old, evento, 0)
                register_service.insert_register(evento)
            except EventoRedZone.DoesNotExist:
                EventoRedZone.objects.create(portal = evento.portal,
                                             tag = evento.tag,
                                             collaborator = evento.collaborator,
                                             sentido = evento.sentido,
                                             temperature = evento.temperature,
                                             battery =  evento.battery,
                                             status = evento.status,
                                             timestamp = evento.timestamp)
                register_service.insert_register(evento)

def collaborators_within_redzone():
    collaborators_in_redzone = EventoRedZone.objects.filter(status=1)
    return collaborators_in_redzone

def collaborators_outside_redzone():
    collaborators_in_redzone = EventoRedZone.objects.filter(status=0)
    return collaborators_in_redzone

def atualizar_evento(evento_antigo, evento_novo, status):
    evento_antigo.portal = evento_novo.portal
    evento_antigo.tag = evento_novo.tag
    evento_antigo.collaborator = evento_novo.collaborator
    evento_antigo.sentido =  evento_novo.sentido
    evento_antigo.temperature =  evento_novo.temperature
    evento_antigo.battery = evento_novo.battery
    evento_antigo.status =  status
    evento_antigo.timestamp = evento_novo.timestamp
    evento_antigo.save(force_update=True)

def create_info_eventos(collaborators_in_redzone, collaborators_out_redzone):

    list_eventos = {
        'qtd_in': len(collaborators_in_redzone),
        'qtd_out': len(collaborators_out_redzone),
        'eventos_in': [],
        'eventos_out': [],
    }

    for evento in collaborators_in_redzone:
        list_eventos['eventos_in'].append({
            'coll_photo' : str(evento.collaborator.foto),
            'coll_full_name': str(evento.collaborator.first_name) + ' '+ str(evento.collaborator.last_name),
            'tag_description': evento.tag.description,
            'tag_battery': evento.battery,
            'tag_temperature': evento.temperature
            })

    for evento in collaborators_out_redzone:
        list_eventos['eventos_out'].append({
            'coll_photo' : str(evento.collaborator.foto),
            'coll_full_name': str(evento.collaborator.first_name) + ' '+ str(evento.collaborator.last_name),
            'tag_description': evento.tag.description,
            'tag_battery': evento.battery,
            'tag_temperature': evento.temperature
            })

    return list_eventos

def remove_evento_redzone(collaborator):
    event_collaborator = EventoRedZone.objects.get(collaborator=collaborator)
    event_collaborator.delete()

def cadastrar_evento_core(type_event, id_event, code, data, date):
    EventoCore.objects.create(type_event=type_event,
                              id_event=id_event,
                              code=code,
                              data=data,
                              date=date)
