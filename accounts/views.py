from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, update_session_auth_hash
from django.contrib import messages
from django.contrib.auth.decorators import login_required, user_passes_test

from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
import json


from .forms import UsuarioForm, LoginForm, ProfilePictureForm
from .entidades.user import User
from .services import usuario_service

#@user_passes_test(lambda u: u.is_superuser)
def cadastrar_usuario(request):
    if request.method == "POST":
        form_usuario = UsuarioForm(request.POST, request.FILES or None)
        if form_usuario.is_valid():
            first_name = form_usuario.cleaned_data["first_name"]
            last_name = form_usuario.cleaned_data["last_name"]
            email = form_usuario.cleaned_data["email"]
            profile_picture = form_usuario.cleaned_data["profile_picture"]
            password = form_usuario.cleaned_data["password1"]
            usuario_novo = User(first_name = first_name, last_name = last_name, email = email, password = password, profile_picture = profile_picture)
            usuario_service.cadastrar_usuario(usuario_novo)
            messages.success(request,  first_name+' '+last_name)
            return redirect('logar_usuario')

    else:

        form_usuario = UsuarioForm()
    return render(request,'user/register.html',{"form_usuario": form_usuario})

def logar_usuario(request):

    if request.method == "POST":
        form_login = LoginForm(data=request.POST)
        if form_login.is_valid():
            username = form_login.cleaned_data["username"]
            password = form_login.cleaned_data["password"]
            usuario = authenticate(request, username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect('home')
            else:
                messages.error(request,'As credenciais do usuário estão incorretas')
                return redirect('logar_usuario')
    else:
        form_login = LoginForm()
    return render(request, 'user/login.html', {"form_login": form_login})

#@login_required()
def deslogar_usuario(request):
    logout(request)
    return redirect('logar_usuario')

def reset_senha_usuario(request):

    if request.method == "POST":
        from_email = 'dagsonmg@gmail.com'
        to_email = request.POST.get('email')
        if from_email:
            usuario = usuario_service.buscar_usuario_email(to_email)
            print(usuario.password)
            send_mail('Solicitação para alterar senha de usuário', 'Sua nova senha é : ', from_email, [to_email], fail_silently=False)
            return redirect('logar_usuario')

    return render(request, 'registration/password_reset_form.html', {})

#@login_required()
def alterar_senha_usuario(request):
    if request.method == "POST":
        form_senha = PasswordChangeForm(request.user, request.POST)
        if form_senha.is_valid():
            user = form_senha.save()
            update_session_auth_hash(request, user)
            return redirect('home')
    else:
        form_senha = PasswordChangeForm(request.user)
    return render(request, 'user/recover-password.html', {'form_senha': form_senha})

#@login_required()
def profile_usuario(request):
       return render(request, 'user/profile_usuario.html',{})

#@login_required()
def atualizar_profile_picture(request):

    if request.method == "POST":
        form_usuario = ProfilePictureForm(request.POST, request.FILES)
        if form_usuario.is_valid():
            profile_picture = form_usuario.cleaned_data["profile_picture"]
            usuario_service.atualizar_foto_prefil(request.user, profile_picture)
            request.session.modified = True
            return redirect('profile_usuario')
    else:
        form_usuario = ProfilePictureForm()
    return render(request, 'user/profile_usuario.html',  {"form_usuario": form_usuario})

