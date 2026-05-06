# Inicializa a variável que vai acumular o total da compra
total = 0

# Loop infinito para manter o programa rodando até o usuário escolher sair
while True:

    # Exibe o menu da lanchonete
    print("\nLANCHONETE")
    print("1 - Coxinha R$ 5,00")
    print("2 - Pastel R$ 7,00")
    print("3 - Café R$ 4,00")
    print("4 - Suco R$ 6,00")
    print("5 - Sair")

    try:
        # Lê a opção escolhida pelo usuário e converte para inteiro
        op = int(input("Qual produto você gostaria de comprar? "))
    except ValueError:
        # Caso o usuário digite algo inválido (letra, símbolo, etc)
        print("Digite um número válido!")
        continue  # Volta para o início do loop

    # Verifica se o usuário quer sair
    if op == 5:
        print("Encerrando o programa...")
        break  # Sai do loop

    # Verifica se a opção está entre 1 e 4 (itens válidos)
    if 1 <= op <= 4:

        try:
            # Pergunta a quantidade desejada
            qtd = int(input("Quantas unidades quer comprar? "))
        except ValueError:
            # Caso a quantidade seja inválida
            print("Quantidade inválida!")
            continue  # Volta para o início do loop

        # Calcula o valor com base na opção escolhida
        if op == 1:
            # Coxinha custa R$ 5,00
            total += qtd * 5.00
        elif op == 2:
            # Pastel custa R$ 7,00
            total += qtd * 7.00
        elif op == 3:
            # Café custa R$ 4,00
            total += qtd * 4.00
        elif op == 4:
            # Suco custa R$ 6,00
            total += qtd * 6.00

    else:
        # Caso o usuário digite um número fora das opções
        print("Opção inválida, tente novamente.")

# Exibe o total final formatado com duas casas decimais
print(f"\nTotal a pagar: R$ {total:.2f}")