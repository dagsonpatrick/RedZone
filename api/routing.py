from django.urls import path

from . import consumers

websocket_urlpatterns = [

    path('ws/redzone/', consumers.MonitoringConsumer),

]