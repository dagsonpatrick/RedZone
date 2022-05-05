from django.db import models


class Tag(models.Model):

    id = models.BigAutoField(primary_key=True)
    description= models.CharField(max_length=50, null=False, blank=False)
    uuid = models.CharField(max_length=15, null=False, blank=False)

    temperature = models.IntegerField(null=True, blank=True)
    battery = models.IntegerField(null=True, blank=True)
    statusAssociacao = models.IntegerField(null=True, blank=True)
    status = models.BooleanField(null=True, blank=True)
    dateCreate = models.DateTimeField(null=False, blank=False, auto_now_add=True)
    dateUpdate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.dateCreate
