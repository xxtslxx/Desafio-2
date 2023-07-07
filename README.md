Sistema Bancário


Este é um sistema bancário simples desenvolvido em Python. Ele permite que você realize operações bancárias básicas, como depósitos, saques e exibição de extratos, além de fornecer a funcionalidade de cadastrar usuários e contas bancárias.

Funcionalidades
O sistema bancário possui as seguintes funcionalidades:

Cadastrar Usuário: Permite cadastrar um novo usuário no sistema fornecendo informações como nome, data de nascimento, CPF e endereço. O sistema verifica se o CPF já foi cadastrado anteriormente para evitar duplicações.

Cadastrar Conta Bancária: Permite vincular uma conta bancária a um usuário existente. Cada usuário pode ter várias contas, desde que cada uma tenha um número de conta diferente. O sistema verifica se o número da conta já foi cadastrado para o usuário em questão.

Depósito: Permite realizar um depósito em uma conta bancária informando o valor desejado. O saldo da conta é atualizado e o valor do depósito é registrado.

Saque: Permite realizar um saque em uma conta bancária informando o valor desejado. O sistema verifica se o valor está dentro do limite máximo permitido por operação (R$ 500,00) e se o saldo da conta é suficiente. O saldo e o valor do saque são atualizados.

Extrato: Exibe o extrato de uma conta bancária, mostrando todos os depósitos e saques realizados, bem como o saldo atual.

