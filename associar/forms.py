from django import forms
from .models import AssociacaoCollaborator

class ColaboradorForm(forms.ModelForm):

    class Meta:
        model = AssociacaoCollaborator
        fields = '__all__'

