from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages import constants
from django.urls import reverse
from django.contrib import auth
from django.contrib.auth.decorators import login_required


def cadastro(request):
    if request.method == 'GET':
        return render(request, 'cadastro.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        senha = request.POST.get('senha')
        confirmar_senha = request.POST.get('confirmar_senha')

        if not senha == confirmar_senha:
            messages.add_message(request, constants.ERROR, 'As senhas não são iguais.')
            return redirect(reverse('cadastro'))
        
        senha = str(senha)

        # TODO: Validar força da senha.

        if len(senha) < 7:
            return redirect(reverse('cadastro'))
        
        user = User.objects.filter(username=username)

        if user.exists():
            messages.add_message(request, constants.ERROR, 'Usuario já existe.')
            return redirect(reverse('cadastro'))

        user = User.objects.create_user(username=username, email=email, password=senha)
        messages.add_message(request, constants.SUCCESS, 'Usuario cadastrado com sucesso!')

        return redirect(reverse('login'))

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        senha = request.POST.get('senha')

        user = auth.authenticate(username=username, password=senha)

        if not user:
            messages.add_message(request, constants.ERROR, 'Usuario ou senha inválidos.')
            return redirect(reverse('login'))

        auth.login(request, user)
        return redirect(reverse('home'))

@login_required    
def logout(request):
    auth.logout(request)
    return redirect(reverse('login'))

