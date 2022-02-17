from ..models import Usuario

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