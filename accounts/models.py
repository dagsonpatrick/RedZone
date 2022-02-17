from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone

from .manager import UsuarioManager
import os
import uuid


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("foto_perfil/", filename)



class Usuario(AbstractBaseUser, PermissionsMixin):

    objects = UsuarioManager()

    email = models.EmailField(unique=True, null=False, blank=False)
    first_name = models.CharField(max_length=15, null=True, blank=False)
    last_name = models.CharField(max_length=15, null=True, blank=False)

    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    #profile_picture = models.ImageField(upload_to='foto_perfil/', null=True, blank=True)
    profile_picture = models.ImageField(upload_to=get_file_path, null=True, blank=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    def __str__(self):
        return self.email





