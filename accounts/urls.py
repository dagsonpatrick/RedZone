from django.conf.urls import url
from django.urls import path, include
from .views import *
from django.contrib.auth.views import PasswordResetView, PasswordResetForm
from django.contrib.auth import views as auth_views
from django.contrib import admin
urlpatterns = [

    path('cadastrar_usuario/', cadastrar_usuario, name='cadastrar_usuario'),
    path('logar_usuario/', logar_usuario, name='logar_usuario'),
    path('deslogar_usuario/', deslogar_usuario, name='deslogar_usuario'),
    path('reset_senha_usuario/', reset_senha_usuario, name='reset_senha_usuario'),
    path('alterar_senha_usuario/', alterar_senha_usuario, name='alterar_senha_usuario'),
    path('profile_usuario/', profile_usuario, name='profile_usuario'),
    path('atualizar_profile_picture/', atualizar_profile_picture, name='atualizar_profile_picture'),


    #path('password_reset/', auth_views.PasswordResetView.as_view(template_name='registration/password_reset_form.html'), name='password_reset'),
    #path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    #path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    #path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),


]