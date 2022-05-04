from django.db import models
from tag.models import Tag
from collaborator.models import Collaborator


class EventoRedZone(models.Model):

    portal = models.CharField(max_length=15, null=False, blank=False)
    tag = models.ForeignKey(Tag, null=False, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, null=True, blank=True, on_delete=models.CASCADE)
    sentido = models.CharField(max_length=15, null=False, blank=False)
    temperature = models.IntegerField(null=False, blank=False)
    battery = models.IntegerField(null=False, blank=False)
    status = models.IntegerField(null=False, blank=False)
    timestamp =  models.DateTimeField(null=True, blank=True)


class EventoCore(models.Model):

    id = models.BigAutoField(primary_key=True)
    type_event = models.CharField(max_length=6, null=False, blank=False)
    id_event = models.CharField(max_length=10, null=False, blank=False)
    code = models.CharField(max_length=6, null=False, blank=False)
    data = models.CharField(max_length=17, null=False, blank=False)
    date = models.DateTimeField(null=False, blank=False)