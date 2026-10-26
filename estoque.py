CAPACIDADE = 10
estoque = 10


def ler_inteiro(mensagem):
    """Pede um número inteiro e repete até o usuário digitar um válido."""
    while True:
        texto = input(mensagem)
        try:
            return int(texto)
        except ValueError:
            print("Digite um número inteiro.")


while True:
    print("""Escolha uma opção:
1 - Adicionar unidades
2 - Remover unidades
3 - Exibir estoque
4 - Sair""")
    escolha = ler_inteiro("Digite a opção desejada: ")
    if escolha == 1:
        qtd = ler_inteiro("Quantas unidades serão adicionadas: ")
        if qtd <= 0:
            print("Digite uma quantidade maior que zero.")
        elif estoque + qtd > CAPACIDADE:
            print(f"Não cabe tudo: o estoque comporta até {CAPACIDADE} unidades.")
        else:
            estoque = estoque + qtd
            print("Unidades adicionadas.")
    elif escolha == 2:
        qtd = ler_inteiro("Quantas unidades serão removidas: ")
        if qtd <= 0:
            print("Digite uma quantidade maior que zero.")
        elif qtd > estoque:
            print("Não há unidades suficientes em estoque.")
        else:
            estoque = estoque - qtd
            print("Unidades removidas.")
    elif escolha == 3:
        print(f"{estoque} unidades em estoque")
    elif escolha == 4:
        print("Saindo do programa.")
        break
    else:
        print("Escolha inválida.")
