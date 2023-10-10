from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from pyzabbix import ZabbixAPI

def logar(usuario, senha, zurl):
    if zurl == 1:
        zapi = ZabbixAPI("https://portal.intradash.com.br/")
        zapi.login(user=usuario, password=senha)

def home(request): 
    if request.method == "GET":
        return render(request, "app.html")
    elif request.method == "POST": 
        usuario1 = request.POST.get("usuario1")
        usuario2 = request.POST.get("usuario2")
        usuario3 = request.POST.get("usuario3")
        
        if usuario1:
            user_id = 273
            updateMedia(usuario1, user_id)
            messages.add_message(request, constants.SUCCESS, 'Telefone 12x36 alterado com sucesso.')
        elif usuario2:
            user_id = 311
            updateMedia(usuario2, user_id)
            messages.add_message(request, constants.SUCCESS, 'Telefone Plantonista N1 alterado com sucesso.')
        elif usuario3:
            user_id = 311
            updateMedia(usuario2, user_id)
            messages.add_message(request, constants.SUCCESS, 'Telefone Plantonista N2 alterado com sucesso.')
        else:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema, contate pessoal responsável.')
            return redirect('/home/app/')
        return redirect('/home/app/')


def updateMedia(usuario, user_id):
    user = "lgti.marcelo.mello"
    passwd = "@Conexao124#%@"
    zapi = ZabbixAPI("https://portal.intradash.com.br/")
    zapi.login(user=user, password=passwd)
    zapi.user.update(
        userid = user_id,
        medias=[{
            "mediatypeid": 6,
            "sendto": usuario,
            "active": 0,
            "severity": 48,
            "period": "1-5,00:00-08:00;1-5,18:00-24:00;6-7,00:00-24:00"
        }]
    )