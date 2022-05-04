from django.urls import path
from .views import EventPortalList, EventPortalDetalhes, EventCoreList

urlpatterns = [
    # API POST
    path('eventos', EventPortalList.as_view(), name='evento-list'),

    # API GET
    path('eventsredzone', EventPortalDetalhes.as_view(), name='evento-detalhes'),

    # API POST - CORE
    path('evento_core', EventCoreList.as_view(), name='evento-core-list')

]