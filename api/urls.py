from django.urls import path
from .views import EventPortalList, EventPortalDetalhes

urlpatterns = [
    # API POST
    path('eventos', EventPortalList.as_view(), name='evento-list'),
    # API GET
    path('eventsredzone', EventPortalDetalhes.as_view(), name='evento-detalhes'),

]