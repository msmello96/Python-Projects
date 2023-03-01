from api_agent import incluir_agente
from api_snmp import incluir_snmp
import validacoes


def main():
    while True:
        print("Bem vindo a inserção de ativos no Zabbix")
        cliente = input("Qual o nome do Cliente: ")
        servico = input("Qual o tipo de Serviço: ")
        groupid = int(input("Informe o ID do Grupo: "))
        templateid = int(input("Informe o ID do Template: "))
        nome_arquivo = input("Informe o nome do arquivo: ")

        print('---------------------------------------------------------')
        print(f"O cliente informado foi: {cliente}")
        print(f"O servico informado foi: {servico}")
        print(f"O ID do gurpo informado foi: {groupid}")
        print(f"O ID do template informado foi: {templateid}")
        print(f"O ID do template informado foi: {nome_arquivo}.csv")

        print('---------------------------------------------------------')
        opcao = int(input("As informações acima estão corretas? [1] SIM | [2] NÃO | [9] SAIR - Digite o numero: "))

        if opcao == 1:
            if servico in validacoes.lista_agent:
                incluir_agente(cliente, servico, groupid, templateid, nome_arquivo)
                break
            elif servico in validacoes.lista_snmp:
                incluir_snmp(cliente, servico, groupid, templateid, nome_arquivo)
                break
            else:
                print('Serviço informado errado, verifique a ortografia.')
        elif opcao == 9:
            break


if __name__ == '__main__':
    main()
