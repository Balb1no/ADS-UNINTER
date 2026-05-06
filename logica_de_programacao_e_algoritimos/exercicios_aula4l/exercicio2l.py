# Loop infinito para repetir o programa várias vezes
while True:
    
    try:
        # Pede um valor inteiro ao usuário
        valor = int(input("Digite o valor (ou 0 para sair): "))
    
    except ValueError:
        # Caso o usuário digite algo que não seja número
        print("Digite apenas números inteiros!")
        continue  # Volta para o início do loop

    # Se o usuário digitar 0, encerra o programa
    if valor == 0:
        print("Encerrando...")
        break  # Sai do while

    # Guarda o valor original (só para mostrar depois)
    original = valor

    # Calcula quantas notas de 100 cabem no valor
    notas100 = valor // 100
    valor = valor % 100  # Pega o resto

    # Calcula notas de 50
    notas50 = valor // 50
    valor = valor % 50

    # Calcula notas de 20
    notas20 = valor // 20
    valor = valor % 20

    # Calcula notas de 10
    notas10 = valor // 10
    valor = valor % 10

    # Calcula notas de 5
    notas5 = valor // 5
    valor = valor % 5

    # O que sobrar são notas de 1
    notas1 = valor

    # Mostra o resultado
    print(f"\nValor: {original}")
    print(f"Notas de 100: {notas100}")
    print(f"Notas de 50: {notas50}")
    print(f"Notas de 20: {notas20}")
    print(f"Notas de 10: {notas10}")
    print(f"Notas de 5: {notas5}")
    print(f"Notas de 1: {notas1}")

    # Linha visual para separar as execuções
    print("-" * 30)