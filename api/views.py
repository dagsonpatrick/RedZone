from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .entidades.eventoredzone import EventosRedZone
from .services import evento_service
from tag.services import tag_service
from associar.services import associar_service
from .serializers import evento_serializer
from django.http import JsonResponse, HttpResponse

#from django.core import serializer

import asyncio
import websockets
import json

async def sendWebsockets(eventos_red_zone):

    strjson = json.dumps(eventos_red_zone)

    uri = "ws://127.0.0.1:8000/ws/redzone/"

    async with websockets.connect(uri) as websocket:
        await websocket.send(strjson)
        await websocket.recv()



class EventPortalList(APIView):

    def post(self, request, format=None):

        lista_eventos = request.data

        for evento in lista_eventos:

            portal = evento.get('portal')
            tag = tag_service.listar_tag_address(evento.get('tag'))
            sentido = evento.get('sentido')
            temperature = evento.get('temperature')
            battery = evento.get('battery')
            timestamp = evento.get('timestamp')

            collaborator_ass_tag = associar_service.buscar_colaborador_ass_tag(tag)
            collaborator = collaborator_ass_tag.collaborator

            if sentido == 'Entrou':
                status_presenca = 1
            else:
                status_presenca = 0



            evento_novo = EventosRedZone(portal=portal,
                                        tag=tag,
                                        collaborator=collaborator,
                                        sentido=sentido,
                                        temperature=temperature,
                                        battery=battery,
                                        status=status_presenca,
                                        timestamp=timestamp)
            evento_service.cadastrar_evento(evento_novo)

            collaborators_in_redzone = evento_service.collaborators_within_redzone()
            collaborators_out_redzone = evento_service.collaborators_outside_redzone()
            eventos_red_zone = evento_service.create_info_eventos(collaborators_in_redzone, collaborators_out_redzone)
            asyncio.new_event_loop().run_until_complete(sendWebsockets(eventos_red_zone))
            #asyncio.get_event_loop().run_until_complete(sendWebsockets(eventos_red_zone))

        return Response("OK", status=status.HTTP_201_CREATED)

class EventPortalDetalhes(APIView):

    def get(self, request, format=None):

        collaborators_in_redzone = evento_service.collaborators_within_redzone()

        collaborators_out_redzone = evento_service.collaborators_outside_redzone()

        eventos_red_zone = evento_service.create_info_eventos(collaborators_in_redzone, collaborators_out_redzone)

        #tmpJson = serializers.serialize("json", collaborators_in_redzone)
        #tmpObj = json.loads(tmpJson)

        return HttpResponse(json.dumps(eventos_red_zone))