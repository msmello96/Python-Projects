from csv import reader
from credenciais import login
from time import sleep
import getpass


def incluir_agente(cliente, servico, groupid, templateid, nome_arquivo):
    with open('arquivos/' + nome_arquivo + '.csv') as arquivo:
        leitor_csv = reader(arquivo)
        next(leitor_csv)
        print("Zabbix: [1] Teste ")
        zurl = int(input("Opção: "))
        usuario = input("Usuario: ")
        senha = getpass.getpass("Senha: ")
        for linha in leitor_csv:
            login(usuario, senha, zurl).host.create(
                host=(cliente + " - " + servico + " - " + linha[0].upper()),
                status=1,
                interfaces=[{
                    "type": 1,
                    "main": "1",
                    "useip": 1,
                    "ip": linha[1],
                    "dns": "",
                    "port": 10050,
                    "details": {
                        "version": 2,
                        "bulk": 1,
                        "community": "{$SNMP_COMMUNITY}"
                    }
                }],
                groups=[{
                    "groupid": groupid,
                }],
                templates=[{
                    "templateid": templateid
                }]
            )
            print(f"Cliente: {cliente} | Serviço: {servico} | Host: {linha[0]} | IP: {linha[1]}")
    print("Fim da execução do programa.")
    sleep(60)
