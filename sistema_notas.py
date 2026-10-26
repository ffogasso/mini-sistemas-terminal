nota = -1  # -1 significa "nenhuma nota registrada ainda"


def ler_inteiro(mensagem):
    """Pede um número inteiro e repete até o usuário digitar um válido."""
    while True:
        texto = input(mensagem)
        try:
            return int(texto)
        except ValueError:
            print("Digite um número inteiro.")


def ler_decimal(mensagem):
    """Pede um número e repete até o usuário digitar um válido."""
    while True:
        texto = input(mensagem).replace(",", ".")
        try:
            return float(texto)
        except ValueError:
            print("Digite um valor numérico.")


while True:
    print("""Sistema de notas
1 - Informar nota
2 - Consultar situação do aluno
3 - Sair""")
    opcao = ler_inteiro("Escolha uma opção: ")
    if opcao == 1:
        temp_nota = ler_decimal("Digite a nota do aluno 0-10: ")
        if temp_nota >= 0 and temp_nota <= 10:
            nota = temp_nota
            print(f"Nota {nota} registrada com sucesso.")
        else:
            print("Valor incorreto, digite novamente.")
    elif opcao == 2:
        if nota == -1:
            print("Nenhuma nota registrada ainda.")
        elif nota >= 7:
            print(f"Aluno aprovado com nota: {nota}")
        elif nota >= 3:
            print(f"Aluno de recuperação com nota: {nota}")
            nota_rec = ler_decimal("Digite a nota do aluno na recuperação: ")
            total = (nota + nota_rec) / 2
            if total > 5:
                print("Aluno aprovado.")
            else:
                print("Aluno reprovado.")
        else:
            print(f"Aluno reprovado diretamente com nota: {nota}")
    elif opcao == 3:
        print("Saindo do sistema.")
        break
    else:
        print("Opção incorreta, tente novamente")
