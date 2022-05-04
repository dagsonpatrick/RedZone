from rest_framework import serializers
from ..models import EventoCore


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = EventoCore
        fields = '__all__'