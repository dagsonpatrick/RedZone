from django.urls import path
from .views import *

urlpatterns = [

    #path('visualizar_planta/', visualizar_planta, name='visualizar_planta'),
    path('monitoring/', monitoring, name='monitoring'),

]