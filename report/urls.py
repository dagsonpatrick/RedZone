from django.urls import path
from .views import pesquisar_timeline, relatorio, pesquisar_registros, export_register_excel


urlpatterns = [

    path('pesquisar_timeline/', pesquisar_timeline, name='pesquisar_timeline'),
    path('relatorio/', relatorio, name='relatorio'),
    path('pesquisar_registros/', pesquisar_registros, name='pesquisar_registros'),
    path('export_register_excel/', export_register_excel, name='export_register_excel')

]
