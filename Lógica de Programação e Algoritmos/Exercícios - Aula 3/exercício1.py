lado1 = int(input("Digite o primeiro lado: "))
lado2 = int(input("Digite o segundo lado: "))
lado3 = int(input("Digite o terceiro lado: "))

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    if lado1 < lado2 + lado3 and lado2 < lado1 + lado3 and lado3 < lado1 + lado2:
        # aqui entra a classificação
        if lado1 == lado2 == lado3:
            print("Equilátero")
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            print("Isósceles")
        else:
            print("Escaleno")
    else:
        print("Não forma triângulo")
else:
    print("Valor inválido")
