from django.db import models

# Create your models here.
class Tag(models.Model):
    id = models.BigAutoField(primary_key=True)
    description= models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=15, null=False, blank=False)
    temperature = models.IntegerField(null=False, blank=False)
    battery = models.IntegerField(null=False, blank=False)
    statusAssociacao = models.IntegerField(null=True, blank=True)
