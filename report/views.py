from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from register.services import register_service
import datetime
import xlwt
from xlwt import *
from django.contrib import messages
from collaborator.services import collaborator_service

global registro_pesquisa, dt_inicial_pesquisa, dtFinal_final_pesquisa


@login_required()
def pesquisar_timeline(request):
    global registro_pesquisa, dt_inicial_pesquisa, dtFinal_final_pesquisa
    horaInicial = '00:00:00'
    horaFinal = '23:59:59'
    collaborators = collaborator_service.listar_collaborators()
    if request.method == "POST":
        strDatas = request.POST.get('reservation')
        collaborator = request.POST.get('collaborator')
        strDatas = strDatas.replace('/', '-')
        dataInicial = strDatas[0:10]
        dtInicial = dataInicial[6:] + '-' + dataInicial[3:5] + '-' + dataInicial[:2] + ' ' + horaInicial
        dataFinal = strDatas[13:]
        dtFinal = dataFinal[6:] + '-' + dataFinal[3:5] + '-' + dataFinal[:2] + ' ' + horaFinal
        dt_inicial_pesquisa = dtInicial
        dtFinal_final_pesquisa = dtFinal
        events = register_service.register_timeline_collaborator(dtInicial, dtFinal, collaborator)
        qtd_events = len(events)
        registro_pesquisa = events
        if events:
            return render(request, 'report/report_timeline_registers.html', {'registros': events,
                                                                            'dataPesquisada': strDatas,
                                                                            'qtd_events' : qtd_events,
                                                                            'visible': 'visible',
                                                                            'collaborators':list(collaborators)})
        else:
            messages.info(request, 'SEM EVENTOS PARA A DATA PESQUISADA')
            return render(request, 'report/report_timeline_registers.html', {'registros': events,
                                                                            'dataPesquisada': strDatas,
                                                                            'qtd_events': qtd_events,
                                                                            'visible':'hidden',
                                                                            'collaborators': collaborators})
    return render(request, 'report/report_timeline_registers.html', {'visible': 'hidden',
                                                                     'collaborators': collaborators })
