#---------------------------------------------------------------------------
# Objetivo: Coletar dados de 4 pessoas e gerar relatórios de média de idade,
#           mulheres jovens e o homem mais velho do grupo.
#---------------------------------------------------------------------------

# Definindo o número de pessoas a serem analisadas
num_pessoas = 4

# Inicializando as variáveis para as análises
soma_idade = 0
contador_mulheres_jovens = 0
maior_idade_homem = 0
nome_homem_mais_velho = ''

# Loop para coletar dados de cada pessoa
for p in range(1, num_pessoas + 1):
    print(f'----- {p}ª PESSOA-----')
    nome = input('Nome: ').strip()
    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').upper().strip()

    # Adiciona a idade para o cálculo da média
    soma_idade += idade

    # Verifica se a pessoa é uma mulher com menos de 20 anos
    if sexo == 'F' and idade < 20:
        contador_mulheres_jovens += 1

    # Identifica o homem mais velho no grupo
    if sexo == 'M':
        if idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_homem_mais_velho = nome.capitalize()

#--------------------------------
# Geração dos Relatórios Finais
#--------------------------------
print('\n')
media_idade = soma_idade / num_pessoas
print(f'A média de idade do grupo é de {media_idade:.2f} anos.')

# Tratamento para o caso de não haver homens no grupo
if maior_idade_homem > 0:
    print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_homem_mais_velho}.')
else:
    print('Não foi informado nenhum homem no grupo.')

print(f'Ao todo são {contador_mulheres_jovens} mulheres com menos de 20 anos.')
