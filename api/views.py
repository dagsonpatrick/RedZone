
from .entidades.eventoredzone import EventosRedZone
from .entidades.evento import Evento
from .services import evento_service
from tag.services import tag_service
from associar.services import associar_service


# from django.shortcuts import render
#from django.core import serializer
from django.http import JsonResponse, HttpResponse


# from rest_framework.parsers import JSONParser
# from rest_framework.decorators import api_view
# from rest_framework.decorators import parser_classes
# from rest_framework.parsers import JSONParser

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework_api_key.permissions import HasAPIKey

import asyncio
import websockets
import json
import datetime

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



class EventCoreList(APIView):

    #@api_view(['POST'])
    #@parser_classes([JSONParser])

    permission_classes = [HasAPIKey]

    def post(self, request, format=None):

        print(f'[INFO] RECEBENDO CHAMADA: {datetime.datetime.now()}')
        print(f'[INFO] DADOS: {request.data}')

        evento = request.data
        type_event = evento.get('type')
        id_event = evento.get('id')
        code = evento.get('code')
        data = evento.get('data')
        date = evento.get('date')
        date = date.replace("T", " ")
        date = date.replace("Z", "")
        uuid = data[:8]
        battery = data[8:]

        # print(f'UUID: {uuid} Tamanho: {len(uuid)}')
        # print(f'BATTERY: {battery} Tamanho: {len(battery)}')
        # 8 primeiros digitos é o UUID (MAC)
        # 8 ultimos é o nivel da bateria em mV (1000mv = 1volt)

        tag = tag_service.buscar_tag_uuid(uuid)

        if tag:
            print('[INFO] TAG EXISTENTE')

            if tag.status and tag.statusAssociacao:
                print('[INFO] TAG ATIVADA E ASSOCIADA A UM COLABORADOR')
                tag_service.atualizar_tag(tag, battery, date)

                tag = tag_service.buscar_tag_uuid(uuid)

                collaborator_ass_tag = associar_service.buscar_colaborador_ass_tag(tag)

                collaborator = collaborator_ass_tag.collaborator

                if code == 101:
                    print(f'[INFO] TAG: {tag.description} ENTRADA Code:{code}')
                    sentido = 'Entrou'
                    status_presenca = 1
                else:
                    status_presenca = 0
                    sentido = 'Saiu'
                    print(f'[INFO] TAG: {tag.description} SAIDA Code:{code}')

                evento_novo = EventosRedZone(portal='01',
                                             tag=tag,
                                             collaborator=collaborator,
                                             sentido=sentido,
                                             temperature=tag.temperature,
                                             battery=battery,
                                             status=status_presenca,
                                             timestamp=tag.dateUpdate)

                evento_service.cadastrar_evento(evento_novo)
                collaborators_in_redzone = evento_service.collaborators_within_redzone()
                collaborators_out_redzone = evento_service.collaborators_outside_redzone()
                eventos_red_zone = evento_service.create_info_eventos(collaborators_in_redzone,
                                                                      collaborators_out_redzone)
                asyncio.new_event_loop().run_until_complete(sendWebsockets(eventos_red_zone))

                evento_service.cadastrar_evento_core(type_event, id_event, code, evento.get('data'), date)

        else:
            print(f'[INFO] TAG NAO EXISTENTE NO BD')
            tag = Evento(type_event, id_event, code, uuid, battery, date)
            tagAuto = tag_service.cadastrar_tag_automatico(tag)
            print(f'[INFO] {tagAuto} CADASTRADA AUTOMATICA')

        print(
            '--------------------------------------------------------------------------------------------------------------')
        retorno = {
            "type": 3,
            "status": 1,
            "date": str(datetime.datetime.now())
        }

        return JsonResponse(retorno)