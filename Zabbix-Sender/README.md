Explicativo do codigo: 
1) O arquivo "main.py" é o arquivo principal e apenas ele que deve ser executado caso estiver usando alguma IDE.
2) O arquivo "validacoes.py" não deve ser alterado nada no código pois este possui as validações dos serviços cadastrados. Caso deseje alterar/incluir a lista de serviços permitidos, alterar dentro dos arquivos correspondentes em "/parametros/nome_do_arquivo" (Atenção: Não alterar o nome dos arquivos).
3) O arquivo "credenciais.py" contém as informações de acesso (URL) dos Zabbix nosso e dos clientes que temos hoje no nosso ambiente.
4) Os arquivos "api_agent.py" e "api_snmp.py" são os arquivos que fazem a inclusão dos hosts no Frontend do Cliente selecionado via API do Zabbix.
5) O diretório "/arquivos" é a pasta que deverá ficar os arquivos formatados .csv, para que o programa consiga ler os arquivo de acordo com o nome informado na hora de executar o código.


Código para rebuildar o programa no Windows:
> pyinstaller --hidden-import pyzabbix --onefile ./main.py --name ZabbixAdd