import random  # Importa a biblioteca para gerar números aleatórios

itens = ('Pedra', 'Papel', 'Tesoura')  # Define as opções em uma tupla para consulta
resultados = []  # Cria uma lista vazia para armazenar quem venceu cada rodada

while True:  # Inicia um loop infinito que só para quando o usuário digitar 0
    print('\n[1] Pedra | [2] Papel | [3] Tesoura | [0] Sair')  # Mostra o menu de opções
    jogador = int(input('Sua jogada: '))  # Lê a escolha do usuário e converte para número inteiro
    
    if jogador == 0:  # Verifica se o jogador quer encerrar o programa
        break  # Sai do loop 'while' imediatamente
    
    if jogador < 1 or jogador > 3:  # Valida se o número digitado está entre 1 e 3
        print('Opção inválida! Tente novamente.')  # Avisa sobre o erro
        continue  # Volta para o início do loop sem executar o resto
        
    computador = random.randint(1, 3)  # O computador sorteia um número aleatório entre 1 e 3
    
    print(f'\nVocê escolheu {itens[jogador-1]}')  # Exibe a escolha do jogador (ajusta índice: 1 vira 0)
    print(f'Computador escolheu {itens[computador-1]}')  # Exibe a escolha sorteada pelo PC
    
    if jogador == computador:  # Caso os números sejam iguais, temos um empate
        print('EMPATE!')  # Avisa que empatou
        resultados.append('Empate')  # Adiciona o resultado na nossa lista histórica
    elif (jogador == 1 and computador == 3) or (jogador == 2 and computador == 1) or (jogador == 3 and computador == 2):
        # Lógica: Pedra ganha de Tesoura, Papel de Pedra, Tesoura de Papel
        print('VOCÊ VENCEU!')  # Informa a vitória do usuário
        resultados.append('Jogador')  # Salva que o jogador ganhou nesta rodada
    else:  # Se não empatou nem o jogador ganhou, o computador venceu
        print('COMPUTADOR VENCEU!')  # Informa a derrota
        resultados.append('Computador')  # Salva que o computador ganhou
        
# --- Finalização do programa após o 'break' ---
print('\n' + '='*20)  # Imprime uma linha decorativa
print(f'TOTAL DE RODADAS: {len(resultados)}')  # Mostra quantas vezes jogaram (tamanho da lista)
print(f'Vitórias do Jogador: {resultados.count("Jogador")}')  # Conta quantas vezes "Jogador" aparece na lista
print(f'Vitórias do Computador: {resultados.count("Computador")}')  # Conta as vitórias da máquina
print(f'Empates: {resultados.count("Empate")}')  # Conta os empates registrados
print('='*20)  # Fecha a decoração visual