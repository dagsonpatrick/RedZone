from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter

from api import routing as apizedzone

application = ProtocolTypeRouter({

    'websocket': AuthMiddlewareStack(URLRouter(apizedzone.websocket_urlpatterns))


})

#URLRouter([
    # url(apizedzone.websocket_urlpatterns),
    # url(apizedzone.websocket_urlpatterns)
    # ])