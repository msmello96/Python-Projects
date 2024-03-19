from django.http import HttpResponse
from django.shortcuts import render
from .models import Pessoa
from django.core.mail import send_mail

def inscricao(request):
    return render(request, 'inscricao.html')

def processa_inscricao(request):
    nome = request.POST.get('nome')
    email = request.POST.get('email')

    pessoa = Pessoa(nome=nome, email=email)
    pessoa.save()

    send_mail('Cadastro Confirmado', 'Seu cadastro foi confirmado com sucesso.', '', recipient_list=[email])

    return HttpResponse('teste')
