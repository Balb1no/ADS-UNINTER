import random  # Biblioteca para gerar escolhas aleatórias (palavras)
import os      # Biblioteca para manipular caminhos de arquivos e pastas do sistema

# --- CONFIGURAÇÃO DE CAMINHOS (Para garantir que os arquivos fiquem na mesma pasta) ---

# Descobre o caminho absoluto da pasta onde este arquivo .py está salvo
DIRETORIO_ATUAL = os.path.dirname(os.path.abspath(__file__))

# Define o caminho completo para o arquivo de palavras na mesma pasta do script
ARQUIVO_PALAVRAS = os.path.join(DIRETORIO_ATUAL, 'palavras.txt')

# Define o caminho completo para o arquivo de scores na mesma pasta do script
ARQUIVO_SCORES = os.path.join(DIRETORIO_ATUAL, 'scores.txt')

# --- FUNÇÕES DE SUPORTE ---

def carregar_palavra():
    """Lê o arquivo de texto e escolhe uma palavra aleatória."""
    try:
        # Abre o arquivo definido no caminho acima para leitura ('r')
        with open(ARQUIVO_PALAVRAS, 'r', encoding='utf-8') as arquivo:
            palavras = arquivo.readlines()  # Cria uma lista onde cada linha é um item
        # Escolhe uma palavra, remove espaços vazios e coloca em maiúsculo
        return random.choice(palavras).strip().upper()
    except FileNotFoundError:
        # Se o arquivo 'palavras.txt' não existir, avisa o usuário e usa uma padrão
        print(f"\nAVISO: Arquivo {ARQUIVO_PALAVRAS} não encontrado! Usando palavra padrão.")
        return "PYTHON"

def salvar_score(nome, pontos):
    """Grava o nome e a pontuação final no arquivo de texto."""
    # O modo 'a' (append) abre o arquivo para escrita sem apagar o que já existe
    with open(ARQUIVO_SCORES, 'a', encoding='utf-8') as arquivo:
        # Escreve a linha formatada e pula uma linha com o '\n'
        arquivo.write(f"Jogador: {nome} | Score: {pontos}\n")

def exibir_scores():
    """Lê e imprime na tela todos os recordes salvos no arquivo."""
    print("\n========= TABELA DE SCORES =========")
    try:
        # Abre o arquivo de scores para leitura
        with open(ARQUIVO_SCORES, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read()  # Lê todo o texto do arquivo
            if not conteudo: # Verifica se o arquivo está vazio
                print("A tabela está vazia. Comece a jogar!")
            else:
                print(conteudo) # Exibe o conteúdo lido
    except FileNotFoundError:
        # Se o arquivo ainda não existir, significa que ninguém jogou ainda
        print("Ainda não existem scores registrados.")
    print("====================================")

# --- LÓGICA DO JOGO ---

def jogar():
    """Executa uma rodada completa do jogo da forca."""
    # Passo 1: Identificar o jogador (Requisito do print {2FE4E6D3-CC6F-490C-8B53-44AED13E6470}.jpg)
    nome = input("\nDigite o nome do jogador: ").strip().capitalize()
    
    # Passo 2: Preparar as variáveis da partida
    palavra_secreta = carregar_palavra() # Busca a palavra no arquivo txt
    letras_certas = ["_" for letra in palavra_secreta] # Cria a lista visual: ['_', '_', '_']
    tentativas_restantes = 6 # Limite de erros antes do enforcamento
    letras_tentadas = [] # Lista para evitar que o jogador repita letras
    pontuacao = 0 # Inicia o score da rodada

    print(f"Olá {nome}! A palavra tem {len(palavra_secreta)} letras.")

    # Passo 3: Loop de repetição da rodada (Enquanto tiver vida e não ganhar)
    while tentativas_restantes > 0 and "_" in letras_certas:
        print(f"\nPalavra: {' '.join(letras_certas)}") # Exibe: P _ T H _ N
        print(f"Erros restantes: {tentativas_restantes}")
        print(f"Letras já digitadas: {letras_tentadas}")

        chute = input("Qual letra você deseja tentar? ").strip().upper()

        # Validações do Chute
        if len(chute) != 1 or not chute.isalpha(): # Verifica se é apenas uma letra
            print("Entrada inválida! Digite apenas uma letra.")
            continue
        if chute in letras_tentadas: # Verifica se já tentou essa letra
            print("Você já tentou essa letra, escolha outra!")
            continue

        letras_tentadas.append(chute) # Adiciona a letra ao histórico de tentativas

        # Verifica se a letra está na palavra
        if chute in palavra_secreta:
            print(f"Boa! A letra '{chute}' está na palavra.")
            # Percorre a palavra secreta para colocar a letra na posição correta
            for indice, letra in enumerate(palavra_secreta):
                if letra == chute:
                    letras_certas[indice] = chute
                    pontuacao += 10 # Ganha 10 pontos por acerto
        else:
            print(f"Putz! A letra '{chute}' não existe aqui.")
            tentativas_restantes -= 1 # Perde uma vida
            pontuacao -= 5 # Perde 5 pontos por erro

    # Passo 4: Finalização e Resultado
    if "_" not in letras_certas:
        print(f"\n🏆 PARABÉNS, {nome}! Você descobriu a palavra: {palavra_secreta}")
        pontuacao += 50 # Bônus por ganhar o jogo
    else:
        print(f"\n💀 FIM DE JOGO! Você foi enforcado. A palavra era: {palavra_secreta}")

    # Passo 5: Salvar Score (Requisito do print {BB1BD337-11D2-49AF-82DC-52B09EE416D1}.jpg)
    score_final = max(0, pontuacao) # Garante que o score não seja negativo
    salvar_score(nome, score_final)
    print(f"Seu score de {score_final} foi salvo com sucesso!")

# --- MENU PRINCIPAL ---

def menu():
    """Exibe o menu inicial do jogo (Requisito do print {F34E7C9F-1240-4F9A-895A-6981D6E6EFBF}.jpg)."""
    while True: # Mantém o programa rodando até escolher SAIR
        print("\n--- MENU JOGO DA FORCA ---")
        print("1. JOGAR")
        print("2. SCORE")
        print("3. SAIR")
        
        escolha = input("Escolha uma opção (1/2/3): ").strip()

        # Estrutura de decisão do menu
        if escolha == '1':
            jogar()
        elif escolha == '2':
            exibir_scores()
        elif escolha == '3':
            print("Obrigado por jogar! Encerrando...")
            break # Quebra o loop While e fecha o programa
        else:
            print("Opção inválida! Por favor, escolha 1, 2 ou 3.")

# Ponto de entrada oficial do script Python
if __name__ == "__main__":
    menu()