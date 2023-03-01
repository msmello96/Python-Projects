# Projeto Loja

A ideia do projeto foi construir um programa onde fosse possível cadastrar produtos no sistema (De maneira única e validada pelo nome, evitando duplicidades), onde, 
esse cadastro dos produtos possuí as informações de Código (Gerado automático pelo sistema), Nome, Tipo do Produto, Peso e Quantidade a ser cadastrada. 


Nesse projeto, também é possível ajustar o estoque do produto cadastrado, podendo aumentar ou diminuir, com validações para não reduzir a quantidade do produto 
abaixo de 0 e não adicionando valores negativos nas operações.


Foi desenvolvido também a parte de cadastro de clientes (De maneira única e validada pelo CPF, evitando duplicidades), onde, o atributo do cliente possui 
Nome, CPF, Idade, E-mail e Endereço. 


Ainda não foi desenvolvido a parte de relação entre Cliente e Produto, será desenvolvido o relacionamento da compra do produto com cliente, tendo assim, uma maneira de histórico de compras e até mesmo relatórios.


Seguindo a lógica do programa, temos este Menu inicial: 
> 
############################
> 
----- Bem vindo a Loja -----
> 
- Informe a opção desejada -
> 
 1 - Cadastrar produto
> 
 2 - Cadastrar cliente
> 
 3 - Listar Produtos
> 
 4 - Listar Clientes
> 
 5 - Ajustar estoque
> 
 6 - Comprar Produtos
> 
 7 - Visualizar Carrinho
> 
 8 - Fechar Pedido
> 
 9 - Sair do sistema
> 
 Opçao desejada: 
> 
 ############################
> 
 Opções: 
 > 
 1 - Cadastro do produto desejado para a loja com validações de nome, onde, não é possível cadastrar dois produtos com o mesmo nome, fazendo validações caso haja uma digitação errada de letras maiusculas gerando duplicidade no programa. 
 > 
 2 - Cadastro de clientes para poder ter um histórico dos clientes da loja, onde, há uma validação em relação ao CPF do cliente que não é permitido cadastro de mais de um cliente com o mesmo CPF.
 > 
 3 - Listagem de produtos cadastrados exibe as informações dos produtos cadastrados, e, caso não haja nenhum produto cadastrado, o programa informa que ainda não há nenhum produto cadastrado.
 > 
 4 - Listagem de clientes cadastrados exibe as informações dos clientes cadastrados, e, caso não haja nenhum cliente cadastrado, o programa informa que ainda não há nenhum clienet cadastrado.
 > 
 5 - Ajustar estoque é a opção para correções e alterações do estoque, podendo incluir ou subtrair um produto. 
 > 
 6 - Comprar produtos permite que o usuário adicione produtos ao carrinho de compras e a quantidade desejada, e, caso queira adicionar mais unidades, o programa incrementa a quantidade de acordo com o que o usuário digitou.
 > 
 7 - Visualizar o carrinho de compras com os produtos cadastrados e as quantidades que foram inseridas no carrinho pelo usuário.
 > 
 8 - Fechar o pedido gerando assim um extrato da venda para o cliente, informando a quantidade de produtos que ele comprou e o valor total da venda. Quando executado esta função, o carrinho é limpo permitindo nova compra e a quantidade de produtos cadastradas é subtraída direto do estoque.
 > 
 9 - Opção que encerra o programa e sai do sistema.

 > 
 > 

Considerações e planos futuros: 
> 
Ainda será feito algumas validações para que não seja possível comprar produtos e deixar o estoque negativo, exemplo: de 10 produtos cadastrados no estoque do sistema, o usuário poderá comprar 10 ou menos, e caso tente comprar 11 ou mais, será emitido um alerta que não deixará efetivar a venda por quantidade insuficiente do estoque.
> 
Adicionar forma de pagamento na hora de fechar a compra.
> 
Pretendo implementar uma relação de cliente e compra de produtos, onde X cliente comprou YZ produtos, para fins de relatorios e conhecimento dos clientes.
> 
Pretendo implementar um campo relatório para mostrar os produtos cadastrados no sistema por "tipo de produto".
> 
Estou estudando banco de dados para fazer uma integração do programa com banco de dados para deixar salvo as operações da loja (Clientes cadastrados, Produtos cadastrados, vendas realizadas, alterações no estoque).
> 
Assim que concluir a etapa do banco de dados, vou criar uma interface Web para o programa utilizando o Django.
>
