from django.db import models
from tag.models import Tag
from collaborator.models import Collaborator


class Register(models.Model):

    portal = models.CharField(max_length=15, null=False, blank=False)
    tag = models.ForeignKey(Tag, null=False, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, null=False, blank=False, on_delete=models.CASCADE)
    sentido = models.CharField(max_length=15, null=False, blank=False)
    temperature = models.IntegerField(null=False, blank=False)
    battery = models.IntegerField(null=False, blank=False)
    timestamp =  models.DateTimeField(null=False, blank=False)
