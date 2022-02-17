import json
from channels.generic.websocket import AsyncWebsocketConsumer

class MonitoringConsumer(AsyncWebsocketConsumer):

    async def connect(self):

        self.room_group_name = 'monitoring_redzone'

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'monitoring_redzone',
                'eventos_red_zone': text_data_json,

            }
        )

    # Receive message from room group
    async def monitoring_redzone(self, event):
        eventos_red_zone = event['eventos_red_zone']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'eventos_red_zone': eventos_red_zone,
        }))