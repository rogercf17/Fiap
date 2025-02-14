eduardo = 0
joao = 0
jose = 0
lucas = 0
nulo = 0
branco = 0
contador = 1
print('Eleições presidenciais 2024')
print('-'*30)
total_eleitores = int(input('Quantas pessoas irão votar? '))
while contador <= total_eleitores:
    print('Digite (1) para votar em Eduardo\nDigite (2) para votar em João\nDigite (3) para votar em José\nDigite (4) para votar em Lucas\nDigite (5) para votar Nulo\nDigite (6) para votar em Branco')
    voto = input('Qual o seu voto? ')
    if voto == '1':
        eduardo += 1
    elif voto == '2':
        joao += 1
    elif voto == '3':
        jose += 1
    elif voto == '4':
        lucas += 1
    elif voto == '5':
        nulo += 1
    else:
        branco += 1
    contador += 1
print('Resultado da votação:')
print(f'Total de votos:\nEduardo: {eduardo}\nJoão: {joao}\nJosé: {jose}\nLucas: {lucas}\nBrancos: {branco}\nNulos: {nulo}')
print(f'Percentual de votos nulos = {(nulo/total_eleitores)*100}%\nPercentual de votos brancos = {(branco/total_eleitores)*100}%')