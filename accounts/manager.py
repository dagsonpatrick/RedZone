from django.contrib.auth.models import BaseUserManager

class UsuarioManager(BaseUserManager):

    def create_user(self, email, first_name=None, last_name=None,  password=None, profile_picture = None):
        if not email:
            raise ValueError("O usuário precisa de um email")
        usuario = self.model(
            first_name = first_name,
            last_name = last_name,
            email= self.normalize_email(email),
            password=password,
            profile_picture=profile_picture
        )
        usuario.is_superuser = False
        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, first_name, last_name,  password):
        usuario = self.create_user(
            first_name = first_name,
            last_name = last_name,
            email= email,
            password=password
        )
        usuario.is_superuser = True
        usuario.set_password(password)
        usuario.save()
        return usuario

