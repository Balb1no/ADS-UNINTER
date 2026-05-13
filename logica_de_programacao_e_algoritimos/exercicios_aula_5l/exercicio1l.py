def validar_positivo(numero):
    """Verifica se o número é um inteiro positivo."""
    # Retorna True se o número for maior ou igual a 0, caso contrário retorna False
    return numero >= 0

def fatorial(n):
    """
    Calcula o fatorial de um número n.
    :param n: O número a ser calculado (deve ser positivo).
    :return: O valor do fatorial de n.
    """
    # Chama a função de validação antes de prosseguir
    if not validar_positivo(n):
        return "Erro: O número deve ser positivo!"

    # O fatorial de 0 ou 1 é sempre 1
    f = 1
    
    # Loop que começa em 'n' e vai multiplicando até chegar em 1
    for i in range(n, 1, -1):
        f *= i  # f recebe o valor de f multiplicado por i
        
    return f # Retorna o resultado final do cálculo

# --- Testando o programa ---

# Pedindo um número ao usuário e convertendo para inteiro
num = int(input("Digite um número inteiro positivo: "))

# Chamando a função fatorial e guardando o resultado
resultado = fatorial(num)

# Exibindo o resultado na tela
print(f"O fatorial de {num} é: {resultado}")

# Exibindo o 'help' da função conforme solicitado no exercício
print("\n--- Help da Função Fatorial ---")
help(fatorial)