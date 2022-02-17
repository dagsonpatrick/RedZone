
from django.db import models
from collaborator.models import Collaborator
from tag.models import Tag

class AssociacaoCollaborator(models.Model):
    id = models.BigAutoField(primary_key=True)
    tag = models.ForeignKey(Tag, null=False,blank=False, on_delete=models.CASCADE)
    collaborator = models.ForeignKey(Collaborator, null=False, on_delete=models.CASCADE)

