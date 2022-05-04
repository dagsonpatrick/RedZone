from ..models import Usuario, Usuario_Acesso
import datetime



def cadastrar_usuario(usuario):
    usuario = Usuario.objects.create_user(first_name=usuario.first_name,
                                          last_name=usuario.last_name,
                                          email=usuario.email,
                                          password=usuario.password,
                                          profile_picture=usuario.profile_picture)


def atualizar_foto_prefil(usuario, profile_picture):
    usuario = Usuario.objects.get(id=usuario.id)
    usuario.profile_picture = profile_picture
    usuario.save(force_update=True)


def buscar_usuario_email(email):
    return Usuario.objects.get(email=email)


def registrar_login_usuario(usuario):
    Usuario_Acesso.objects.create(usuario = usuario)


def registrar_logout_usuario(id):
    timestamp = datetime.datetime.now()
    user = Usuario.objects.get(id=id)
    usuario = Usuario_Acesso.objects.filter(usuario=user).order_by("-date_login").first()
    usuario.date_logout = timestamp.strftime("%Y-%m-%d %H:%M:%S")
    usuario.save(force_update=True)


def listar_acessos_usuarios():
    return Usuario_Acesso.objects.order_by("id").all()


def listar_usuarios(request):
    lista_userAuth = Usuario.objects.exclude(email=request.user.email).all()
    usuarios = Usuario.objects.filter(email__in=[id for id in lista_userAuth]).all()
    return usuarios


def listar_usuario_id(id):
    return Usuario.objects.get(id=id)


def remover_usuario(usuario):
    usuario.delete()


def desativar_usuario(usuario):
    usuario.is_active=0
    usuario.save(force_update=True)


def ativar_usuario(usuario):
    usuario.is_active=1
    usuario.save(force_update=True)


def pesquisar_acessos_usuarios(dtInicial, dtFinal):
    return Usuario_Acesso.objects.filter(date_login__range=[dtInicial, dtFinal])
