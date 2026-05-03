consumo = int(input("Digite a quantidade de kWh consumida: "))
tipo = input("Digite o tipo de instalação (R, C ou I): ")

if tipo == "R":
    if consumo <= 500:
        valor = 0.40
    else:
        valor = 0.65
    print(f"O valor a ser pago é: R$ {consumo * valor}")

elif tipo == "C":
    if consumo <= 1000:
        valor = 0.55
    else:
        valor = 0.60
    print(f"O valor a ser pago é: R$ {consumo * valor}")

elif tipo == "I":
    if consumo <= 5000:
        valor = 0.55
    else:
        valor = 0.60
    print(f"O valor a ser pago é: R$ {consumo * valor}")

else:
    print("Tipo de instalação inválido.")