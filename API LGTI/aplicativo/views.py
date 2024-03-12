from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.messages import constants
from django.contrib import auth
from pyzabbix import ZabbixAPI
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

@login_required(login_url='/')
def alteracao(request): 
    """
        Função que detém a lógica e funcionamento do código, recebimento dos parâmetros digitados pelo usuário no 
        frontend, validação dos dados se existem e se são númericos, sendo aceito apenas números.
        Configuração da constante "nome_usuario" e "nome_midia" que são definidos no código e padronizado nos 
        ambientes Zabbix como indicativo ao usuário que será alterado a mídia e o tipo da mídia, sendo a ligação, 
        padronizado como "Ligação Webhook 2" em todos os ambientes. 
        Em sequência, as variáveis "user_id" e "midia_id" são a chamada das respectivas funções para obter o ID do 
        usuário e o ID do tipo de mídia de acordo com as strings passadas através da constante "nome_usuario" e 
        "nome_midia".
        Após obter as informações do retorno das funções acima, é chamado a função "updateMedia" para executar 
        a alteração nos usuários em todos os ambientes.
    """

    if request.method == "GET":
        return render(request, "app.html")
    elif request.method == "POST": 
        usuario1 = request.POST.get("usuario1")
        usuario2 = request.POST.get("usuario2")
        usuario3 = request.POST.get("usuario3")
        
        if usuario1:
            if usuario1.isnumeric():
                nome_usuario = os.getenv("ZBX_USER1")
                nome_midia = os.getenv("ZBX_MIDIA")
                
                i = 1
                ambientes = [1, 2, 3, 4, 5, 6, 7]
                for i in ambientes: 
                    user_id = getUserId(nome_usuario, i)
                    media_id = getMidiaId(nome_midia, i)
                    updateMedia(usuario1, user_id, media_id, i)
                    i+= i

                messages.add_message(request, constants.SUCCESS, 'Telefone 12x36 alterado com sucesso.')
                return redirect('/app')
            else:
                messages.add_message(request, constants.ERROR, 'Digite um número de telefone válido.')
        
        elif usuario2:
            if usuario2.isnumeric():
                nome_usuario = os.getenv("ZBX_USER2")
                nome_midia = os.getenv("ZBX_MIDIA")
                
                i = 1
                ambientes = [1, 2, 3, 4, 5, 6, 7]
                for i in ambientes: 
                    user_id = getUserId(nome_usuario, i)
                    media_id = getMidiaId(nome_midia, i)
                    updateMedia(usuario2, user_id, media_id, i)
                    i+= i

                messages.add_message(request, constants.SUCCESS, 'Telefone Plantonista N1 alterado com sucesso.')
                return redirect('/app/')
            else:
                messages.add_message(request, constants.ERROR, 'Digite um número de telefone válido.')
       
        elif usuario3:
            if usuario3.isnumeric():
                nome_usuario = os.getenv("ZBX_USER3")
                nome_midia = os.getenv("ZBX_MIDIA")
                
                i = 1
                ambientes = [1, 2, 3, 4, 5, 6, 7]
                for i in ambientes: 
                    user_id = getUserId(nome_usuario, i)
                    media_id = getMidiaId(nome_midia, i)
                    updateMedia(usuario3, user_id, media_id, i)
                    i+= i
                    
                messages.add_message(request, constants.SUCCESS, 'Telefone Plantonista N2 alterado com sucesso.')
                return redirect('/app/')
            else:
                messages.add_message(request, constants.ERROR, 'Digite um número de telefone válido.')
        
        else:
            messages.add_message(request, constants.ERROR, 'Erro interno do sistema, contate pessoal responsável.')
            return redirect('/app/')
        
        return redirect('/app/')

def logar(zurl):
    """
        Função que tem as credenciais de acesso do usuário que irá realizar o login através da API do Zabbix e 
        o indicativo de todos os ambientes configurados que serão alterados os números de telefone. 
    """

    usuario = os.getenv("ZBX_LOGIN")
    senha = os.getenv("ZBX_SENHA")

    if zurl == 1:
        zapi = ZabbixAPI(os.getenv("ZBX_ZURL1"))
        zapi.login(user=usuario, password=senha)
        return zapi
    
    elif zurl == 2:
        zapi = ZabbixAPI(os.getenv("ZBX_ZURL2"))
        zapi.login(user=usuario, password=senha)
        return zapi
    
    elif zurl == 3:
        zapi = ZabbixAPI(os.getenv("ZBX_ZURL3"))
        zapi.login(user=usuario, password=senha)
        return zapi
   
    elif zurl == 4:
        zapi = ZabbixAPI(os.getenv("ZBX_ZURL4"))
        zapi.login(user=usuario, password=senha)
        return zapi
    
    elif zurl == 5:
        zapi = ZabbixAPI(os.getenv("ZBX_ZURL5"))
        zapi.login(user=usuario, password=senha)
        return zapi
    
    elif zurl == 6:
        zapi = ZabbixAPI(os.getenv("ZBX_ZURL6"))
        zapi.login(user=usuario, password=senha)
        return zapi
    
    elif zurl == 7:
        zapi = ZabbixAPI(os.getenv("ZBX_ZURL7"))
        zapi.login(user=usuario, password=senha)
        return zapi
 
def getUserId(username, zurl):
    """
        Função que pega o ID do usuário de acordo com o primeiro parâmetro "username", passado através de uma 
        string constante dentro do código, na função "alteracao". Seguido pelo ambiente que está buscando o usuário, 
        no segundo parâmetro "zurl", onde, percorre todos os ambientes configurados na função "logar".
    """
    retorno = logar(zurl).user.get(
        output=["userid", "username"],
        filter=[{"login": username}]
    )

    for usuario in retorno:
        if usuario["username"] == username:
            return usuario["userid"]

def getMidiaId(media, zurl):
    """
        Função que pega o ID do tipo de mídia de acordo com o primeiro parâmetro "media", passado através de uma 
        string constante dentro do código, na função "alteracao". Seguido pelo ambiente que está buscando a midia, 
        no segundo parâmetro "zurl", onde, percorre todos os ambientes configurados na função "logar".
    """
    retorno = logar(zurl).mediatype.get(
        filter={"name": media}
    )

    return retorno[0]["mediatypeid"]

def updateMedia(telefone, user_id, media_id, zurl):
    """
        Função que executa as alterações das midias dentro de cada usuário informado nos ambientes Zabbix, 
        recebendo o telefone digitado pelo usuário, os parâmetros obtidos dos retornos das funções "getUserID" e 
        "getMidiaId", sendo ID do usuário e ID da mídia respectivamente, seguido pelo indicativo do ambiente através 
        do parâmetro da função "zurl".
    """
    logar(zurl).user.update(
        userid = user_id,
        medias=[{
            "mediatypeid": media_id,
            "sendto": telefone,
            "active": 0,
            "severity": 48,
            "period": "1-5,00:00-08:00;1-5,18:00-24:00;6-7,00:00-24:00"
        }]
    )

@login_required(login_url='/')
def sair(request):
    """
        Função que faz o logout do usuário do sistema. 
    """
    auth.logout(request)
    return redirect('/')
