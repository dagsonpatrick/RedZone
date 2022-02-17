from rest_framework import serializers
from ..models import EventoRedZone


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventoRedZone
        fields = '__all__'