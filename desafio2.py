class Usuario:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

class ContaBancaria:
    def __init__(self, usuario, numero_conta):
        self.usuario = usuario
        self.numero_conta = numero_conta
        self.saldo = 0.0
        self.saques_realizados = []
        self.depositos_realizados = []

    def deposito(self, valor):
        self.saldo += valor
        self.depositos_realizados.append(valor)

    def saque(self, valor):
        if valor > 500.0:
            print("O valor máximo de saque é de R$ 500,00 por operação.")
            return
        if len(self.saques_realizados) >= 3:
            print("Você já realizou o máximo de saques permitidos por dia.")
            return
        if self.saldo < valor:
            print("Saldo insuficiente.")
            return

        self.saldo -= valor
        self.saques_realizados.append(valor)

    def extrato(self):
        print("Extrato:")
        if not self.saques_realizados and not self.depositos_realizados:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos_realizados:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques_realizados:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


class Banco:
    def __init__(self):
        self.contas = []

    def cadastrar_usuario(self, nome, data_nascimento, cpf, endereco):
        for conta in self.contas:
            if conta.usuario.cpf == cpf:
                print("CPF já cadastrado.")
                return

        usuario = Usuario(nome, data_nascimento, cpf, endereco)
        conta_bancaria = ContaBancaria(usuario, None)
        self.contas.append(conta_bancaria)
        print("Usuário cadastrado com sucesso.")

    def cadastrar_conta_bancaria(self, cpf, numero_conta):
        for conta in self.contas:
            if conta.usuario.cpf == cpf:
                if conta.numero_conta == numero_conta:
                    print("Número de conta já cadastrado para esse usuário.")
                    return

        for conta in self.contas:
            if conta.usuario.cpf == cpf:
                conta.numero_conta = numero_conta
                print("Conta bancária cadastrada com sucesso.")
                return

        print("Usuário não encontrado.")

    def encontrar_conta(self, cpf, numero_conta):
        for conta in self.contas:
            if conta.usuario.cpf == cpf and conta.numero_conta == numero_conta:
                return conta

        return None


banco = Banco()

while True:
    print("1. Cadastrar Usuário")
    print("2. Cadastrar Conta Bancária")
    print("3. Depósito")
    print("4. Saque")
    print("5. Extrato")
    print("6. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome do usuário: ")
        data_nascimento = input("Digite a data de nascimento do usuário: ")
        cpf = input("Digite o CPF do usuário: ")
        endereco = input("Digite o endereço do usuário: ")
        banco.cadastrar_usuario(nome, data_nascimento, cpf, endereco)
    elif opcao == "2":
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta bancária: ")
        banco.cadastrar_conta_bancaria(cpf, numero_conta)
    elif opcao == "3":
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta bancária: ")
        valor = float(input("Digite o valor do depósito: "))
        conta = banco.encontrar_conta(cpf, numero_conta)
        if conta:
            conta.deposito(valor)
        else:
            print("Conta bancária não encontrada.")
    elif opcao == "4":
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta bancária: ")
        valor = float(input("Digite o valor do saque: "))
        conta = banco.encontrar_conta(cpf, numero_conta)
        if conta:
            conta.saque(valor)
        else:
            print("Conta bancária não encontrada.")
    elif opcao == "5":
        cpf = input("Digite o CPF do usuário: ")
        numero_conta = input("Digite o número da conta bancária: ")
        conta = banco.encontrar_conta(cpf, numero_conta)
        if conta:
            conta.extrato()
        else:
            print("Conta bancária não encontrada.")
    elif opcao == "6":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")
