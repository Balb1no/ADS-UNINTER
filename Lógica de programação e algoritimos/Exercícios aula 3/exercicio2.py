valor1 = int(input("Digite o primeiro valor: "))
valor2 = int(input("Digite o segundo valor: "))
operador = input("Digite o operador (+, -, *, /): ")

if operador == "+":
    resultado = valor1 + valor2
    print("O resultado é:", resultado)
elif operador == "-":
    resultado = valor1 - valor2
    print("O resultado é:", resultado)
elif operador == "*":
    resultado = valor1 * valor2
    print("O resultado é:", resultado)
elif operador == "/":
    if valor2 != 0:
        resultado = valor1 / valor2
        print("O resultado é:", resultado)
    else:
        print("Erro: não é possível dividir por zero.")
else:
    print("Operador inválido.")