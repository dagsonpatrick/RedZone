from django.urls import path
from .views import pesquisar_timeline


urlpatterns = [

    path('pesquisar_timeline/', pesquisar_timeline, name='pesquisar_timeline'),

]
