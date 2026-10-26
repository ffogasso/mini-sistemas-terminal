saldo = 2000.0


def ler_inteiro(mensagem):
    """Pede um número inteiro e repete até o usuário digitar um válido."""
    while True:
        texto = input(mensagem)
        try:
            return int(texto)
        except ValueError:
            print("Digite um número inteiro.")


def ler_decimal(mensagem):
    """Pede um valor em reais e repete até o usuário digitar um número válido."""
    while True:
        texto = input(mensagem).replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Digite um valor numérico.")


while True:
    print("""Caixa eletrônico
1 - Consultar saldo
2 - Depositar
3 - Sacar
4 - Sair""")
    opcao = ler_inteiro("Escolha uma opção: ")
    if opcao == 1:
        print(f"Seu saldo é de: R$ {saldo:.2f}")
        if saldo <= 0:
            print("Você não possui saldo.")
    elif opcao == 2:
        deposito = ler_decimal("Digite o valor do depósito: ")
        if deposito <= 0:
            print("Valor inválido, tente novamente")
        else:
            saldo = saldo + deposito
            print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == 3:
        saque = ler_decimal("Digite o valor do saque: ")
        if saque <= 0:
            print("Valor inválido, tente novamente")
        elif saque > saldo:
            print("Saldo insuficiente.")
        else:
            saldo = saldo - saque
            print(f"Saldo atual: R$ {saldo:.2f}")
    elif opcao == 4:
        print("Saindo do sistema")
        break
    else:
        print("Opção inválida, tente novamente.")
