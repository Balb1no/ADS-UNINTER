# Definimos o nome do arquivo que guardará os dados no computador
ARQUIVO = "Lógica de programação e algoritimos/Exercícios aula 5/jogos.txt"

# --- FUNÇÃO PARA CADASTRAR ---
def cadastrar_novo():
    """Função para coletar dados e salvar no disco"""
    nome_jogo = input("Nome do jogo: ")  # Lê o nome do jogo
    plataforma = input("Videogame: ")    # Lê o console/plataforma
    
    # Abrimos o arquivo no modo 'a' (append) para adicionar sem apagar o anterior
    # 'with' garante que o arquivo seja fechado automaticamente ao final
    with open(ARQUIVO, "a", encoding="utf-8") as f:
        # Escrevemos os dados formatados com uma quebra de linha (\n) no final
        f.write(f"{nome_jogo} | {plataforma}\n")
    
    print("Item cadastrado com sucesso!\n")

# --- FUNÇÃO PARA LISTAR ---
def listar_tudo():
    """Função para ler o arquivo e exibir os itens na tela"""
    print("\n--- LISTA DE JOGOS CADASTRADOS ---")
    try:
        # Abrimos para leitura ('r' de read)
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            linhas = f.readlines()  # Transforma cada linha do arquivo em um item de lista
            
            if not linhas:  # Se a lista estiver vazia
                print("A lista está vazia.")
            else:
                for item in linhas:
                    # strip() remove espaços e quebras de linha invisíveis
                    print(item.strip()) 
    except FileNotFoundError:
        # Se o arquivo ainda não existir, tratamos o erro amigavelmente
        print("Ainda não existem cadastros no sistema.")
    print("-" * 30 + "\n")

# --- FUNÇÃO DO MENU (PRINCIPAL) ---
def iniciar_menu():
    """Função que controla o fluxo do algoritmo"""
    while True:  # Loop infinito para o menu rodar até o usuário decidir sair
        print("1 - Cadastrar novo item")
        print("2 - Listar tudo")
        print("3 - Sair")
        
        escolha = input("Escolha (1/2/3): ")  # Captura a opção do usuário
        
        if escolha == '1':
            cadastrar_novo()  # Chama a função de cadastro
        elif escolha == '2':
            listar_tudo()     # Chama a função de listagem
        elif escolha == '3':
            print("Saindo...")
            break             # Interrompe o loop 'while' e encerra o programa
        else:
            print("Opção inválida! Tente de novo.\n")

# Comando que realmente inicia a execução do programa chamando o menu
iniciar_menu()