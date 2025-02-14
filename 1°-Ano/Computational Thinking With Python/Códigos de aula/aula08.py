'''
def cria_naipe(naipe):
    lista_final = []
    for carta in ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']:
        lista_final.append(f'{carta} de {naipe.title()}')
    # return ' | '.join(lista_final)
    return lista_final
def cria_baralho():
    baralho = []
    for naipe in ['ouros', 'espada', 'copas', 'zap']:
        # baralho.extend(cria_naipe(naipe))
        baralho.append(cria_naipe(naipe))
    # return '\n'.join(baralho)
    return baralho
baralho = cria_baralho()
print(baralho)
print(type(baralho[0]))
print(baralho[2][3])
print(baralho[1][1])
'''

'''
FOR ENCADEADO
1 - Escreva uma função que recebe um número, 
e retorna uma lista de strings que representa 
a tabuada desse número (ex: tabuada_do(3) retorna [3x1=3, 3x2=6...])
def tabuada(numero):
    for c in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        print(f'{numero} x {c} = {numero*c}')
tabuada(3)

2 - Escreva uma função que retorna uma lista 
com todas as tabuadas, do 1 ao 10
def tabuada_um_a_dez():
    lista = []
    for c in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            resultado = f'{c} x {i} = {c*i}'
            lista.append(resultado)
    return lista
lista = tabuada_um_a_dez()
print('\n'.join(lista))

3- Escreva uma função que recebe um número, 
e devolve True se ele é primo, False, caso contrário
def verifica_primo(numero):
    numeros_divisiveis = 0
    for divisor in range(1, numero+1):
        if numero%divisor == 0:
            numeros_divisiveis += 1      
    if numeros_divisiveis > 2:
        resultado = False
    else:
        resultado = True 
    return 'Não é primo' if resultado == False else 'É primo'
resultado = verifica_primo(7)
resultado2 = verifica_primo(10)
print(resultado)
print(resultado2)

4 - Escreva uma função que recebe um número, e devolve 
uma lista de todos os primos até esse limite. 
Se primos(100), retornaremos a lista de todos os primos menores que 100
def cria_lista_primos(numero):
    lista_primos = []
    for numero_dividendo in range(1, numero):
        numero_divisiveis = 0
        for numero_divisor in range(1, numero):
            if numero_dividendo % numero_divisor == 0:
                numero_divisiveis += 1
        if numero_divisiveis == 2:
            lista_primos.append(numero_dividendo)
    return lista_primos
print(cria_lista_primos(100))

5 - Faça uma função palindromo, que recebe uma string e responde True se ela é um palindromo, 
False caso contrário. Palindromo é uma string espelhada. palindromo(“aba”) deve retornar True, 
palindromo(“abacate”) deve retornar false
def verifica_palimdromo(string):
    palavra = string.lower()
    palavra_invertida = palavra[::-1]
    return 'É palímdromo' if palavra == palavra_invertida else 'Não é palímdromo'
print(verifica_palimdromo('Ana'))
print(verifica_palimdromo('Roger'))

6 - Faça uma função maior palindromo, 
que retorna o maior palindromo que podemos achar, 
considerando o começo de uma string
Por exemplo, maior_palindromo(abacate) deve retornar aba 

7 - Faça uma função soma_faixa que recebe um limite superior, um limite inferior e uma lista, 
e devolve a soma dos numeros nessa faixa.
Por exemplo soma_faixa([10,20,30,40,50],1,4) pega os indices 1,2 e 3, 
ou seja, os números 20, 30, 40, produzindo a soma 90
def soma_faixa(lista, limite_inferior, limite_superior):
    soma = 0
    for i in range(limite_inferior, limite_superior):
        soma += lista[i]
    return soma
print(soma_faixa([10,20,30,40,50],1,4))

8 - Faça uma função maior faixa, que acha a faixa com a soma maior possível
dentro de uma lista, e devolve essa soma


9 - Faça uma função que recebe um tamanho, e devolve uma string representando 
uma linha com tamanho pontos. linha(3) vai retornar a string '...'
def criar_linha(tamanho):
    linha = '.' * tamanho
    return linha
print(criar_linha(50))

10 - Faça uma função que recebe um comprimento e uma altura, e devolve 
uma string representando um 'mapa' com aquele comprimento e altura. 
mapa(3,4) vai retornar a string '...\n...\n...\n...\n'
def cria_mapa(comprimento, altura):
    mapa = ('.'*comprimento+'\n') * altura
    return mapa
print(cria_mapa(20,5))
'''

