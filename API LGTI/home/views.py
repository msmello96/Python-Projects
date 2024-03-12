from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib.messages import constants
from django.contrib import messages

def logar(request):
    """
        Essa é a função de login no sistema, utilizando a tabela de autenticação do próprio Django. 
        A criação dos logins é feita a partir do cadastro de um super usuário que, após isso, cria 
        os outros usuários através da área administrativa.
    """
    
    if request.method == "GET":
        if request.user.is_authenticated:
            return redirect('/app')
        return render(request, 'home.html')
    elif request.method == "POST":
        username = request.POST.get('usuario')
        senha = request.POST.get('senha')
        usuario = auth.authenticate(username=username, password=senha)

        if not usuario:
            messages.add_message(request, constants.ERROR, 'Username ou senha inválidos')
            return redirect('/')
        else:
            auth.login(request, usuario)
            return redirect('/app')
    