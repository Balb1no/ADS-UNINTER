from datetime import datetime  # Importamos para pegar o ano atual automaticamente

# Criamos o dicionário onde as chaves são as categorias e os valores são listas vazias
dados = {'nomes': [], 'idades': [], 'sexos': []}

while True:  # Loop para cadastrar quantas pessoas o usuário quiser
    nome = str(input('Nome: '))  # Lê o nome da pessoa
    ano_nasc = int(input('Ano de Nascimento: '))  # Lê o ano de nascimento
    sexo = str(input('Sexo [M/F]: ')).upper().strip()[0]  # Lê o sexo, padroniza e pega a 1ª letra
    
    idade = datetime.now().year - ano_nasc  # Calcula a idade baseada no ano atual do sistema
    
    # Adicionamos cada informação na sua respectiva lista dentro do dicionário
    dados['nomes'].append(nome)
    dados['idades'].append(idade)
    dados['sexos'].append(sexo)
    
    # Pergunta se o usuário quer continuar cadastrando
    continuar = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if continuar == 'N':  # Se a resposta for 'N' (Não), quebra o loop
        break

# --- Cálculos dos Resultados ---

total_cadastros = len(dados['nomes'])  # O total é o tamanho de qualquer uma das listas
media_idade = sum(dados['idades']) / total_cadastros  # Soma as idades e divide pelo total

# Criamos listas vazias para os filtros específicos solicitados
mulheres_menos_30 = []
homens_acima_media = []

# Percorremos as listas usando o índice (i) para relacionar os dados de cada pessoa
for i in range(total_cadastros):
    # Regra: Mulheres (F) com menos de 30 anos
    if dados['sexos'][i] == 'F' and dados['idades'][i] < 30:
        mulheres_menos_30.append(dados['nomes'][i])
    
    # Regra: Homens (M) com idade acima da média do grupo
    if dados['sexos'][i] == 'M' and dados['idades'][i] > media_idade:
        homens_acima_media.append(dados['nomes'][i])

# --- Exibição Final dos Resultados ---

print('-=' * 30)
print(f'A) Total de cadastros efetuados: {total_cadastros}')
print(f'B) Média das idades: {media_idade:.2f} anos')
print(f'C) Mulheres com menos de 30 anos: {mulheres_menos_30}')
print(f'D) Homens com idade acima da média: {homens_acima_media}')
print('-=' * 30)