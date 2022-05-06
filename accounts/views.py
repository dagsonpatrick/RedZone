from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test
from django.core.mail import send_mail
from django.http import HttpResponse
import datetime
from .forms import UsuarioForm, LoginForm, ProfilePictureForm
from .entidades.user import User
from .services import usuario_service
from xlwt import *
import xlwt


global registros_acesso, dt_inicial_pesquisa, dt_final_pesquisa

#@user_passes_test(lambda u: u.is_superuser)
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(request.POST, request.FILES or None)
        if form_usuario.is_valid():
            first_name = form_usuario.cleaned_data["first_name"]
            last_name = form_usuario.cleaned_data["last_name"]
            email = form_usuario.cleaned_data["email"]
            profile_picture = form_usuario.cleaned_data["profile_picture"]

            # Usuário não adicionou foto de perfil
            if profile_picture is None:

                if first_name[-1:] == 'a' or first_name[-1:] == 'A':
                    profile_picture = "foto_perfil/avatar_feminino.png"
                else:
                    profile_picture = "foto_perfil/avatar_masculino.png"

            password = form_usuario.cleaned_data["password1"]
            usuario_novo = User(first_name = first_name, last_name = last_name, email = email, password = password, profile_picture = profile_picture)
            usuario_service.cadastrar_usuario(usuario_novo)
            messages.success(request,  first_name+' '+last_name)
            messages.info(request, email)
            return redirect('logar_usuario')
    else:
        form_usuario = UsuarioForm()
    return render(request,'user/register.html',{"form_usuario": form_usuario})

def logar_usuario(request):
    if request.method == "POST":
        form_login = LoginForm(data=request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data["username"]
            password = form_login.cleaned_data["password"]
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                usuario_service.registrar_login_usuario(usuario)
                return redirect('home')
        else:
            messages.error(request, 'as credenciais do usuário estão incorretas')
            return redirect('logar_usuario')
    else:
        form_login = LoginForm()
    return render(request, 'user/login.html', {"form_login": form_login})

#@login_required()
def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')

def reset_senha_usuario(request):

    if request.method == "POST":
        from_email = 'dagsonmg@gmail.com'
        to_email = request.POST.get('email')
        if from_email:
            usuario = usuario_service.buscar_usuario_email(to_email)
            print(usuario.password)
            send_mail('Solicitação para alterar senha de usuário', 'Sua nova senha é : ', from_email, [to_email], fail_silently=False)
            return redirect('logar_usuario')

    return render(request, 'registration/password_reset_form.html', {})

#@login_required()
def alterar_senha_usuario(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'user/recover-password.html', {'form_senha': form_senha})

#@login_required()
def profile_usuario(request):
       return render(request, 'user/profile_usuario.html',{})

#@login_required()
def atualizar_profile_picture(request):

    if request.method == "POST":
        form_usuario = ProfilePictureForm(request.POST, request.FILES)
        if form_usuario.is_valid():
            profile_picture = form_usuario.cleaned_data["profile_picture"]
            usuario_service.atualizar_foto_prefil(request.user, profile_picture)
            request.session.modified = True
            return redirect('profile_usuario')
    else:
        form_usuario = ProfilePictureForm()
    return render(request, 'user/profile_usuario.html',  {"form_usuario": form_usuario})

@login_required()
def listar_usuarios(request):
    usuarios = usuario_service.listar_usuarios(request)
    return render(request, 'user/form_listar_usuarios.html', {"usuarios": usuarios})


@login_required()
def remover_usuario(request, id):
    usuario = usuario_service.listar_usuario_id(id)
    if request.method == "POST":
        usuario_service.remover_usuario(usuario)
        return redirect('listar_usuarios')
    return render(request, 'user/confirma_exclusao_user.html', {'usuario':usuario})


@login_required()
def desativar_usuario(request, id):
    usuario = usuario_service.listar_usuario_id(id)
    usuario_service.desativar_usuario(usuario)
    return redirect('listar_usuarios')


@login_required()
def ativar_usuario(request, id):
    usuario = usuario_service.listar_usuario_id(id)
    usuario_service.ativar_usuario(usuario)
    return redirect('listar_usuarios')


@login_required()
def add_permission_admin(request, id):
    usuario_service.add_permission_admin(id)
    return redirect('listar_usuarios')

@login_required()
def add_permission_base(request, id):
    usuario_service.add_permission_base(id)
    return redirect('listar_usuarios')


@login_required()
def listar_acessos_usuarios(request):
    global registro_pesquisa
    acessos = usuario_service.listar_acessos_usuarios()
    return render(request, 'user/form_listar_acessos_usuarios.html', {'acessos': acessos, 'visible': 'hidden'})


@login_required()
def pesquisar_acessos_usuarios(request):
    global registros_acesso, dt_inicial_pesquisa, dt_final_pesquisa
    acessos = usuario_service.listar_acessos_usuarios()
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
        dt_final_pesquisa = dtFinal
        registros_acesso = usuario_service.pesquisar_acessos_usuarios(dtInicial, dtFinal)
        if registros_acesso:
            return render(request, 'user/form_listar_acessos_usuarios.html', {'acessos': registros_acesso,
                                                                              'dataPesquisada': strDatas,'visible': 'visible'})
        else:
            messages.info(request, 'SEM ACESSO PARA A DATA PESQUISADA')
            return render(request, 'user/form_listar_acessos_usuarios.html', {'acessos': registros_acesso,
                                                                              'dataPesquisada': strDatas,
                                                                              'visible': 'hidden'})


@login_required()
def export_excel(request):

    global registros_acesso, dt_inicial_pesquisa, dt_final_pesquisa

    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=Relatório de Acesso Sistema.xls'
    wb = xlwt.Workbook(encoding='utf-8')

    timestampInicial = datetime.datetime.strptime(dt_inicial_pesquisa, '%Y-%m-%d %H:%M:%S')
    timestampFinal = datetime.datetime.strptime(dt_final_pesquisa, '%Y-%m-%d %H:%M:%S')
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
    ws.merge(0, 0, 0, 2, styleA4solutions)

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

    ws.write(1, 0, 'Relatório de Acesso ao Sistema', styleSistema)

    ws.merge(1, 1, 0, 2, styleSistema)
    ws.col(0).width = 7000
    ws.col(1).width = 7000
    ws.col(2).width = 7000

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

    columns = ['Usuário', 'Login Data/Hora', 'Logout Data/Hora']
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

    usuario_service.pesquisar_acessos_usuarios(dt_inicial_pesquisa, dt_final_pesquisa)
    rows = registros_acesso.values_list('usuario', 'date_login', 'date_logout')

    for row in rows:
        row_num += 1
        if row_num % 2 == 0:
            pat2.pattern_fore_colour = xlwt.Style.colour_map['white']
            styleDados.pattern = pat2
        if row_num % 2 == 1:
            pat3.pattern_fore_colour = 0x01F
            styleDados.pattern = pat3
        for col_num in range(len(row)):
            if col_num == 1:
                timestamp = datetime.datetime.strptime(str(row[col_num]), '%Y-%m-%d %H:%M:%S.%f')
                data_pt_br = timestamp.strftime("%d/%m/%Y %H:%M:%S")
                ws.write(row_num, col_num, str(data_pt_br), styleDados)
            elif col_num == 2 and row[col_num] == None:
                ws.write(row_num, col_num, 'Usuário não fez Logout', styleDados)
            elif col_num == 2 and row[col_num] != None:
                timestamp = datetime.datetime.strptime(str(row[col_num]), '%Y-%m-%d %H:%M:%S')
                data_pt_br = timestamp.strftime("%d/%m/%Y %H:%M:%S")
                ws.write(row_num, col_num, str(data_pt_br), styleDados)
            else:
                ws.write(row_num, col_num, str(row[col_num]), styleDados)

    wb.save(response)

    return response
