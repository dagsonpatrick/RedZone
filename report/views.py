from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render


import datetime
import xlwt
from xlwt import *
from django.contrib import messages
from collaborator.services import collaborator_service
from register.services import register_service


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


@login_required()
def relatorio(request):
    registros = register_service.listar_register()
    return render(request, 'report/report_registers.html', {'registros': registros,
                                                            'visible': 'hidden',
                                                            })


@login_required()
def pesquisar_registros(request):
    global registro_pesquisa, dt_inicial_pesquisa, dtFinal_final_pesquisa

    horaInicial = '00:00:00'
    horaFinal = '23:59:59'

    if request.method == "POST":
        strDatas = request.POST.get('reservation')
        strDatas = strDatas.replace('/', '-')
        dataInicial = strDatas[0:10]
        dtInicial = dataInicial[6:] + '-' + dataInicial[3:5] + '-' + dataInicial[:2] + ' ' + horaInicial
        dataFinal = strDatas[13:]
        dtFinal = dataFinal[6:] + '-' + dataFinal[3:5] + '-' + dataFinal[:2] + ' ' + horaFinal
        dt_inicial_pesquisa = dtInicial
        dtFinal_final_pesquisa = dtFinal
        events = register_service.events_register(dtInicial, dtFinal)
        qtd_events = len(events)
        registro_pesquisa = events
        if events:
            return render(request, 'report/report_registers.html', {'registros': events,
                                                                    'dataPesquisada': strDatas,
                                                                    'qtd_events' : qtd_events,
                                                                    'visible': 'visible'})
        else:
            messages.info(request, 'SEM EVENTOS PARA A DATA PESQUISADA')
            return render(request, 'report/report_registers.html', {'registros': events,
                                                                    'dataPesquisada': strDatas,
                                                                    'qtd_events': qtd_events,
                                                                    'visible':'hidden'})


@login_required()
def export_register_excel(request):
    global registro_pesquisa, dt_inicial_pesquisa, dtFinal_final_pesquisa
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Relatório Eventos.xls'
    wb = xlwt.Workbook(encoding='utf-8')
    timestampInicial = datetime.datetime.strptime(dt_inicial_pesquisa, '%Y-%m-%d %H:%M:%S')
    timestampFinal = datetime.datetime.strptime(dtFinal_final_pesquisa, '%Y-%m-%d %H:%M:%S')
    dataInit = timestampInicial.strftime("%d-%m-%Y")
    dataFim = timestampFinal.strftime("%d-%m-%Y")
    ws = wb.add_sheet(str(dataInit) + '->' + str(dataFim))

    # Formataçao Texto A4 Solutions
    xlwt.add_palette_colour("custom_colour", 0x21)
    wb.set_colour_RGB(0x21, 111, 66, 193)

    fnt1 = Font()
    fnt1.name = 'Verdana'
    fnt1.bold = True
    fnt1.height = 18 * 0x14
    fnt1.colour_index = xlwt.Style.colour_map['white']

    al1 = Alignment()
    al1.horz = Alignment.HORZ_CENTER
    al1.vert = Alignment.VERT_CENTER

    pat1 = Pattern()
    pat1.pattern = Pattern.SOLID_PATTERN
    pat1.pattern_fore_colour = xlwt.Style.colour_map['custom_colour']

    brd1 = Borders()
    brd1.left = 0x06
    brd1.right = 0x06
    brd1.top = 0x06
    brd1.bottom = 0x06

    styleA4solutions = XFStyle()
    styleA4solutions.font = fnt1
    styleA4solutions.alignment = al1
    styleA4solutions.pattern = pat1
    styleA4solutions.borders = brd1

    ws.write(0, 0, 'A4 SOLUTIONS', styleA4solutions)
    ws.merge(0, 0, 0, 5, styleA4solutions)

    # Formatação Texto Sistema de Deteção de Fumaça
    fnt2 = Font()
    fnt2.name = 'Verdana'
    fnt2.bold = True
    fnt2.italic = True
    fnt2.height = 16 * 0x14

    brd2 = Borders()
    brd2.left = 0x01
    brd2.right = 0x01
    brd2.top = 0x01
    brd2.bottom = 0x01

    pat2 = Pattern()
    pat2.pattern = Pattern.SOLID_PATTERN
    pat2.pattern_fore_colour = 0x01F

    styleSistema = XFStyle()
    styleSistema.font = fnt2
    styleSistema.alignment = al1
    styleSistema.pattern = pat2
    styleSistema.borders = brd2

    ws.write(1, 0, 'Relatório de Eventos', styleSistema)

    ws.merge(1, 1, 0, 5, styleSistema)
    ws.col(0).width = 7000
    ws.col(1).width = 7000
    ws.col(2).width = 7000
    ws.col(3).width = 7000
    ws.col(4).width = 7000
    ws.col(5).width = 7000

    # Formataçao Cabeçalho Planilha
    fnt2 = Font()
    fnt2.name = 'Verdana'
    fnt2.bold = True
    fnt2.height = 14 * 0x14

    brd2 = Borders()
    brd2.left = 0x01
    brd2.right = 0x01
    brd2.top = 0x01
    brd2.bottom = 0x01

    pat2 = Pattern()
    pat2.pattern = Pattern.SOLID_PATTERN
    pat2.pattern_fore_colour = xlwt.Style.colour_map['gray25']

    styleCabecalho = XFStyle()
    styleCabecalho.font = fnt2
    styleCabecalho.alignment = al1
    styleCabecalho.pattern = pat2
    styleCabecalho.borders = brd2

    row_num = 2
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Colaborador', 'RedZone', 'TAG', 'Bateria', 'Temperatura', 'Data/Hora']
    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], styleCabecalho)

    # Formataçao dos Dados
    fnt3 = Font()
    fnt3.name = 'Verdana'
    fnt3.bold = False
    fnt3.italic = False
    fnt3.height = 10 * 0x14

    brd3 = Borders()
    brd3.left = 0x07
    brd3.right = 0x07
    brd3.top = 0x07
    brd3.bottom = 0x07

    pat3 = Pattern()
    pat3.pattern = Pattern.SOLID_PATTERN
    pat3.pattern_fore_colour = xlwt.Style.colour_map['white']

    styleDados = XFStyle()
    styleDados.font = fnt3
    styleDados.alignment = al1
    styleDados.pattern = pat3
    styleDados.borders = brd2

    #rows = registro_pesquisa.values_list('collaborator', 'sentido', 'tag', 'battery', 'temperature', 'timestamp')
    rows = register_service.normalizer_register_export_excel(registro_pesquisa)
    for row in rows:
        row_num += 1
        if row_num % 2 == 0:
            pat2.pattern_fore_colour = xlwt.Style.colour_map['white']
            styleDados.pattern = pat2
        if row_num % 2 == 1:
            pat3.pattern_fore_colour = 0x01F
            styleDados.pattern = pat3
        for col_num in range(len(row)):
            if col_num == 5:
                timestamp = datetime.datetime.strptime(str(row[col_num]), '%Y-%m-%d %H:%M:%S')
                data_pt_br = timestamp.strftime("%d/%m/%Y %H:%M:%S")
                ws.write(row_num, col_num, str(data_pt_br), styleDados)
            else:
                ws.write(row_num, col_num, str(row[col_num]), styleDados)

    wb.save(response)
    return response