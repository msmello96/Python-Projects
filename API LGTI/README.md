# Zabbix Telefonia

## Introdução

Projeto desenvolvido para automatizar a alteração dos números de telefone dos plantonitas e dos colaboradores 12x36, utilizando [Python](https://python.org/) e [Django](https://www.djangoproject.com/) como Framework possibilitando a organização e estruturação do código em conjunto com a segurança oferecida pelo framework.

## Estrutura

A estrutura do projeto foi seguindo os padrões de desenvolvimento do Django, sendo eles cada funcionalidade dividada por APP para manter o código mais limpo e organizado, tendo cada APP a sua funcionalidade especifica apenas. 
O Django utiliza a estutura `MVT (Model, View e Template)`.
> [!NOTE]
>Model: as configurações de tabelas no banco de dados.
>
>View: onde é códificado todo o backend.
> 
>Template: As páginas HTML do frontend.
> 


Neste projeto, temos 2 APPs criados até o momento: `aplicativo` e `home`. 

O APP `home` está codificado as partes de login e redirecionamento para o APP `aplicativo`, utilizando as tabelas de autenticação padrão do proprio Django. 

O APP `aplicativo` está a lógica e a parte robusta do backend, tendo as funções declaradas de obter ID do usuário, ID da mídia, funções de login dos ambientes, função de update da mídia dentro de cada usuário e a função de alteração que está a lógica e as validações necessárias para que ocorra tudo conforme planejado nas chamadas das funções para executar as mudanças de mídia nos usuários desejados.

Foi utilizado também a biblioteca [dotenv](https://pypi.org/project/python-dotenv/) para poder aumentar a segurança do projeto sem a necessidade de compartilhamento das informações sensíveis dentro do código.

Na parte do frontend, foi utilizado HTML e CSS para estruturar e estilizar as páginas. 

## Deploy

O deploy da aplicação foi feito em [Docker](https://www.docker.com/), utilizado como microserviço, e hospedado na núvem do [Azure](https://portal.azure.com/) na Tenant da LGTI.

## Utilização

Para utilizar o programa e toda a sua facilidade, o colaborador precisa de um usuário para logar no sistema através da página de home do projeto, e, após validado suas credenciais, o usuário estará em uma tela onde tem 3 opções auto-explicativas para alteração dos números do atendente 12x36 ou plantonista N1 e N2. 
Ao clicar no botão "Alterar" a frente do respectivo usuário que deseja alterar o número de telefone, abrirá uma nova janela para digitar o número de telefone desejado, sendo este campo limitado a 12 caractéres (DDD + Número telefone, ex: 016123451234) e somente números. Digitado os números do telefone, basta apenas clicar novamente no botão verde "Alterar" e aguardar a conclusão do processo, que demora em torno de 5 a 10 segundos, obtendo uma mensagem na tela de que foi alterado com sucesso o número do usuário desejado.
