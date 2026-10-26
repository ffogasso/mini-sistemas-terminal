def ler_inteiro(mensagem):
    """Pede um número inteiro e repete até o usuário digitar um válido."""
    while True:
        texto = input(mensagem)
        try:
            return int(texto)
        except ValueError:
            print("Digite um número inteiro.")


while True:
    print("""Calculadora
1 - Somar
2 - Subtrair
3 - Multiplicar
4 - Dividir
5 - Sair""")
    escolha = ler_inteiro("Escolha uma opção: ")
    if escolha == 1:
        num_1 = ler_inteiro("Digite o primeiro número: ")
        num_2 = ler_inteiro("Digite o segundo número: ")
        soma = num_1 + num_2
        print(f"Resultado: {soma}")
    elif escolha == 2:
        num_1 = ler_inteiro("Digite o primeiro número: ")
        num_2 = ler_inteiro("Digite o segundo número: ")
        subtrair = num_1 - num_2
        print(f"Resultado: {subtrair}")
    elif escolha == 3:
        num_1 = ler_inteiro("Digite o primeiro número: ")
        num_2 = ler_inteiro("Digite o segundo número: ")
        multiplicar = num_1 * num_2
        print(f"Resultado: {multiplicar}")
    elif escolha == 4:
        num_1 = ler_inteiro("Digite o primeiro número: ")
        num_2 = ler_inteiro("Digite o segundo número: ")
        if num_2 == 0:
            print("Não é possível dividir por zero.")
        else:
            dividir = num_1 / num_2
            print(f"Resultado: {dividir}")
    elif escolha == 5:
        print("Saindo da calculadora.")
        break
    else:
        print("Escolha incorreta.")
