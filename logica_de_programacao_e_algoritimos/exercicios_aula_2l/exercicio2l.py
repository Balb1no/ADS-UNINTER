km = float(input("Digite a distância em km: "))
dias = int(input("Digite a quantidade de dias: "))
preco_km = 0.15
preco_dia = 60
total = (km * preco_km) + (dias * preco_dia)

print(f"Distância percorrida: {km} km e dias de aluguel: {dias} dias")
print(f"O total a pagar é: R$ {total:.2f}")