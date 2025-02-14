'''
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = []
pares2 = []
impares = []
impares2 = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
        continue
    impares.append(i)
print(numeros)
print(pares)
print(impares)
print()
for e in range(len(numeros)):
    if numeros[e] % 2 == 0:
        pares2.append(numeros[e])
        continue
    impares2.append(numeros[e])
print(numeros)
print(pares)
print(impares)
--------------------------------------------------------
# Jeito 1
professores = ['Caio', 'Danilo', 'Lucas', 'Lucas.S', 'Jones']
materias = ['WebDev', 'Python', 'Edge', 'FrontEnd', 'Calculo']
professor_digitado = input('Diga o nome do seu professor: ')
while not professor_digitado in professores:
    print('Professor não encontrado!')
    professor_digitado = input('Diga o nome do seu professor: ')
for i in range(len(professores)):
    if professor_digitado == professores[i]:
        print(f'O {professor_digitado} dá {materias[i]}')
        continue
# Jeito 2
professores = ['Caio', 'Danilo', 'Lucas', 'Lucas.S', 'Jones']
materias = ['WebDev', 'Python', 'Edge', 'FrontEnd', 'Calculo']
achou = False
while not achou:
    professor_digitado = input('Diga o nome do seu professor: ')
    for i in range(len(professores)):
        if professores[i] == professor_digitado:
            print(f'O {professor_digitado} dá {materias[i]}')
            achou = True
            break
--------------------------------------------------------
lista_de_carros = ['Uno', 'Corsa', 'Hb20', 'Gol', 'Sandero']
lista_preco_carros = [48, 29, 85, 54, 68]
def verifica_maior_preco(lista_preco, lista_carro):
    maior_preco = lista_preco_carros[0]
    carro = lista_de_carros[0]
    for c in range(len(lista_preco)):
        if lista_preco[c] > maior_preco:
            maior_preco = lista_preco[c]
            carro = lista_carro[c]
    return print(f'O {carro} é o carro mais caro da lista, custando {maior_preco} mil reais.')
verifica_maior_preco(lista_preco_carros, lista_de_carros)
--------------------------------------------------------
lista_de_carros = ['Uno', 'Corsa', 'Hb20', 'Gol', 'Sandero']
lista_preco_carros = [48, 29, 85, 54, 68]
lista_ano_fabricacao_carros = [2001, 2010, 2015, 2007, 2016]
local_maior = 0
maior = lista_preco_carros[local_maior]
carro = ''
ano = 0
for i in range(len(lista_preco_carros)):
    if lista_preco_carros[i] > maior:
        maior = lista_preco_carros[i]
        carro = lista_de_carros[i]
        ano = lista_ano_fabricacao_carros[i]
        local_maior = i
print(carro, maior, ano)
--------------------------------------------------------
def checaNumero(mensagem, mensageg_erro):
    numero = input(mensagem)
    while not numero.isnumeric():
        print(mensageg_erro)
        numero = input(mensagem)
    return int(numero)
qntd = checaNumero('Diga a quantidade de garrafas: ', 'Quantidade de garrafas inválida! Digite novamente.')
print(qntd)
idade = checaNumero('Diga a sua idade: ', 'Idade inválida! Digite novamente.')
print(idade)
if idade < 18:
    print('Você não pode beber, saia daquiiiiiiiiiiiiiiii!')
else:
    print('Vamos continuar')
--------------------------------------------------------
def checaOpcao(lista, mensagem, mensagem_erro):
    opcao = input(mensagem)
    while not opcao in lista:
        print(mensagem_erro)
        opcao = input(mensagem)
    return opcao
a = checaOpcao(['Pizza', 'Hamburguer', 'Hot Dog', 'Esfiha', 'Sopa'], 'O que deseja pedir p/ comer? ', 'não está na lista, peça outra coisa.')
print(f'Foi escolhido {a}')
b = checaOpcao(['Sim', 'Não', 'sim', 'não'], 'Diga sim ou Não: ', 'É para dizer apenas Sim/sim ou Não/não!')
print(f'Resposta: {b}')
--------------------------------------------------------
lista_vinhos = ['Tinto', 'Rose', 'Branco']
lista_preco_vinhos = [60, 47, 80]
lista_ano_vinho = [2020, 2018, 2022]
def checa_vinho(lista, mensagem):
    escolha = input(mensagem)
    while escolha not in lista:
        escolha = input(mensagem)
    for i in range(len(lista)):
        if escolha == lista[i]:
            indice = i
    return indice
resposta = checa_vinho(lista_vinhos, 'Qual vinho quer comprar? ')
print(f'indice do {lista_vinhos[resposta]} é {resposta} custa {lista_preco_vinhos[resposta]} reais e é de {lista_ano_vinho[resposta]}')
--------------------------------------------------------
lista_de_carros = ['Uno', 'Corsa', 'Hb20', 'Gol', 'Sandero']
marcas = ['Adidas', 'Nike', 'Joma', 'Umbro', 'Puma']
preco_marcas = [100, 120, 70, 85, 90]
lista_preco_carros = [48, 29, 85, 54, 68]
def verifica_maior_preco(lista1, lista2):
    maior_preco = lista1[0]
    for c in range(len(lista1)):
        if lista1[c] > maior_preco:
            maior_preco = lista1[c]
            indice = c
    return f'O {lista2[indice]} é o mais caro da lista, custando {maior_preco} mil reais.'
resposta = verifica_maior_preco(lista_preco_carros, lista_de_carros)
print(resposta)
print()
a = verifica_maior_preco(preco_marcas, marcas)
print(a)
--------------------------------------------------------
numeros = [1,2,3,4,5,6,7,8,9]
def inverte_lista(lista):
    ultimo = len(lista) - 1
    for i in range(len(lista)-5):
        aux = lista[i]
        lista[i] = lista[ultimo-i]
        lista[ultimo-i] = aux
    return lista
resposta = inverte_lista(numeros)
print(resposta)
'''

