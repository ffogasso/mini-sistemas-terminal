cebolinha = 0
gohan = 0
athena = 0

while True:
    print("""
    1 - Cebolinha
    2 - Gohan
    3 - Athena
    4 - Sair
    """)
    opcao = input("Digite seu voto: ")
    if opcao == "1":
        print("Você votou em Cebolinha")
        cebolinha = cebolinha + 1
        print(f"Votos Cebolinha: {cebolinha}")
    elif opcao == "2":
        print("Você votou em Gohan")
        gohan = gohan + 1
        print(f"Votos Gohan: {gohan}")
    elif opcao == "3":
        print("Você votou em Athena")
        athena = athena + 1
        print(f"Votos Athena: {athena}")
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida, tente novamente.")

print(f"\nResultado final -> Cebolinha: {cebolinha} | Gohan: {gohan} | Athena: {athena}")
