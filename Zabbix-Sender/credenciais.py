from pyzabbix import ZabbixAPI


def login(usuario, senha, zurl):
    """if zurl == 1:
        zapi = ZabbixAPI("https://cliente.com.br/")
        zapi.login(user=usuario, password=senha)

        return zapi
    elif zurl == 2:
        zapi = ZabbixAPI("https://cliente.com.br/")
        zapi.login(user=usuario, password=senha)

        return zapi
    elif zurl == 3:
        zapi = ZabbixAPI("https://cliente.com.br/")
        zapi.login(user=usuario, password=senha)

        return zapi
    elif zurl == 4:
        zapi = ZabbixAPI("https://cliente.com.br/")
        zapi.login(user=usuario, password=senha)

        return zapi
    elif zurl == 5:
        zapi = ZabbixAPI("http://cliente.com.vc/")
        zapi.login(user=usuario, password=senha)

        return zapi"""
    # AMBEINTE DE TESTE E DESENVOLVIMENTO
    if zurl == 1:
        zapi = ZabbixAPI("http://40.121.36.202/zabbix")
        zapi.login(user=usuario, password=senha)

        return zapi
