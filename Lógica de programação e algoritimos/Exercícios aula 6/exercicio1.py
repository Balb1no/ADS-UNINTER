# Criamos uma tupla chamada 'palavras' contendo 10 strings (palavras)
palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado')

# Iniciamos um loop para percorrer cada 'p' (palavra) dentro da nossa tupla 'palavras'
for p in palavras:
    # Exibimos o nome da palavra atual. O 'upper()' deixa em maiúsculo e o 'end' evita que o print pule linha
    print(f'\nNa palavra {p.upper()} temos as vogais: ', end='')
    
    # Iniciamos outro loop para percorrer cada 'letra' dentro da palavra atual 'p'
    for letra in p:
        # Verificamos se a letra (convertida para minúsculo) está na string 'aeiou'
        if letra.lower() in 'aeiou':
            # Se for uma vogal, imprimimos a letra seguida de um espaço, mantendo na mesma linha
            print(letra, end=' ')