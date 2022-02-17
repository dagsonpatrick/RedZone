from django.db import models
import os
import uuid


def get_file_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("fotoPerfilColaborador/", filename)


# Create your models here.
class Collaborator(models.Model):
    id = models.BigAutoField(primary_key=True)
    first_name = models.CharField(max_length=15, null=False, blank=False)
    last_name = models.CharField(max_length=15, null=False, blank=False)
    email =  models.EmailField(max_length=70, null=False, blank=False)
    foto = models.FileField(null=True, blank=True, upload_to=get_file_path)
    statusAssociacao = models.IntegerField(null=True, blank=True)


