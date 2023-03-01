"""
NÃO ALTERAR NADA NESSA PARTE
"""

# Validações Lista Agent
arquivo_agent = open('parametros/servicos_agent')
serv_agent = arquivo_agent.readlines()
serv_agent = [x.rstrip('\n') for x in serv_agent]
lista_agent = []

for linha in serv_agent:
    lista_agent.append(linha)


# Validações Lista SNMP
arquivo_snmp = open('parametros/servicos_snmp')
serv_snmp = arquivo_snmp.readlines()
serv_snmp = [x.rstrip('\n') for x in serv_snmp]
lista_snmp = []

for linha in serv_snmp:
    lista_snmp.append(linha)
