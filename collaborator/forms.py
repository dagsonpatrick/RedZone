from django import forms
from .models import Collaborator

class CollaboratorForm(forms.ModelForm):

    class Meta:
        model = Collaborator
        fields = '__all__'