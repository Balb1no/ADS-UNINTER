total_arrecadado = 0  # Inicializa a soma do dinheiro acumulado
total_pessoas = 0     # Inicializa o contador de pessoas que compraram ingresso
soma_idades = 0       # Inicializa a soma das idades para calcular a média depois

while True:           # Inicia um laço de repetição infinito (será parado pelo break)
    idade = int(input("Digite a idade (ou 0 para encerrar): ")) # Pede a idade e converte para número inteiro
    
    if idade == 0:    # Verifica se a idade digitada foi zero
        break         # Sai do laço de repetição imediatamente
    
    # Processamento dos valores do ingresso
    if idade < 3:     # Se a idade for menor que 3 anos
        preco = 0     # O ingresso é gratuito
        print("Ingresso gratuito!")
    elif idade <= 12: # Se a idade estiver entre 3 e 12 (já sabemos que é >= 3)
        preco = 15    # O ingresso custa R$ 15
        print("Preço do ingresso: R$ 15")
    else:             # Se a idade for maior que 12 anos
        preco = 30    # O ingresso custa R$ 30
        print("Preço do ingresso: R$ 30")
    
    # Atualização das estatísticas
    total_arrecadado += preco    # Adiciona o preço atual ao total arrecadado
    total_pessoas += 1           # Incrementa o contador de pessoas
    soma_idades += idade         # Adiciona a idade atual à soma total de idades

# Cálculos finais após o encerramento do laço
if total_pessoas > 0:            # Verifica se pelo menos uma pessoa comprou ingresso para evitar erro de divisão por zero
    media_idade = soma_idades / total_pessoas # Calcula a média aritmética das idades
    
    print("\n--- Resumo do Dia ---")
    print(f"Total de pessoas: {total_pessoas}")
    print(f"Total arrecadado: R$ {total_arrecadado}")
    print(f"Média de idade: {media_idade:.2f} anos")
else:
    print("Nenhum ingresso foi vendido.")