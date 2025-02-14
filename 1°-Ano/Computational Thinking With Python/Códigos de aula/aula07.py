'''Revisão de funções
1. Abra esse arquivo no pycharm
2. Clique com o botão direito no arquivo, e escolha 'run file in python console'
3. No novo terminal que abrir, digite soma(1,2). O resultado deverá ser 3.
Experimente soma(4,5), soma(100,1), soma(-4,6). Não altere a função soma
que está no arquivo!
'''

'''def soma(a,b):
    resultado = a+b    #linha1
    return resultado   #linha2'''

'''
4. O que aconteceu foi o seguinte: quando você digita soma(1,2) naquele novo
terminal, a função soma é chamada. Ela guarda o valor 1 na variavel a e o
valor 2 na variavel b, e começa a executar os comandos da função.
Na linha 2, ela devolveu um número. Foi esse número que
foi impresso no terminal.
5. Primeiro erro comum: testar uma função atribuindo valores de
variáveis dentro da função
O jeito certo de passar números para funções
é chamar a função colocando os números no parenteses,
como fizemos no terminal.
Você não precisa E NAO DEVE colocar na propria função
'''

'''def soma_zoada(a,b):
    #linha 0
    a=2 #linha 1
    b=5 #linha 2
    resultado = a+b    
    return resultado'''   

'''
6. Lá no terminal, rode soma_zoada1(100,10), depois
soma_zoada(12,1). Ela sempre devolve o mesmo número!
7. O que está acontecendo ao rodar soma_zoada1(100,10)?
Na linha 0, a vale 100 e b vale 10. Mas nas linhas 1 e 2, nós 
colocamos 2 no a e 5 no b. Assim, colocamos 7 no resultado.
Resumindo: os números não entram na hora que você monta a função.
Entram depois, quando você for usar a função.
8. O segundo erro comum é usar input. Input pode ser útil as vezes,
mas quando eu digo 'faça uma função que recebe dois números e retorna a soma'
eu *sempre* quero dizer que ela recebe como argumento, não fia input.
Os números devem entrar no parênteses ao chamar a função. Não de outra forma.
9. Uma coisa muito util é chamar uma função dentro de outra.
Não que o exemplo a seguir seja muito útil :P
'''

'''def soma3(a,b,c):
    dois_primeiros = soma(a,b)
    resultado = soma(dois_primeiros,c)
    return resultado'''
'''

10. Vá no terminal e experimente soma3(4,2,1),
soma3(9,3,10)...
11. Usando o que você relembrou até agora, escreva uma função 
quadrado que recebe um número e o eleva ao quadrado.
No momento, a função está errada. Corrija
'''

'''def quadrado(a):
    resposta = a**2
    return resposta'''

'''
12. Clique 'run python file in console' de novo. Você tem que fazer
isso toda vez que alterar o arquivo, para o python carregar suas
alterações.
13. Teste no terminal do run module (chame: quadrado(2), 
. Depois, SEM ALTERAR O ARQUIVO, SO MEXENDO NO TERMINAL, quadrado(3)). 
14. Faça mais testes, a gosto.
15. Agora que você testou, se sua função parece OK, rode,
no terminal a função runTests (faça isso digitando
runTests())
16. Se a sua função estava dando respostas certas, sem você ter
que mudar nada dentro dela, talvez o seu erro seja
que você usou print(resposta) ao invés de return resposta
17. Mas, se deu certo, vou definir uma função que usa a sua
'''

'''def pitagoras(cate1, cate2):
    return raiz(quadrado(cate1)+quadrado(cate2))
import math
def raiz(n):
    return math.sqrt(n)'''

'''
17. Teste a função pitagoras, fazendo
pitagoras(3,4) 
pitagoras(4,3) -> os dois tem que dar 5
pitagoras(1,1) -> tem que dar raiz de 2. Confira na calculadora. do celular

se nao estiver dando certo, você se lembrou de testar sua
função quadrado com o runTests? Se nao, volte para o passo 15
(ou mesmo para o 13)
'''

'''
18. Agora, sem olhar o codigo acima, tente definir uma função
soma_dos_quadrados que receba dois numeros
e devolva a soma dos seus quadrados.
'''
'''def soma_dos_quadrados(a,b):
    soma_quadrados = quadrado(a) + quadrado(b)
    return soma_quadrados'''
'''
19. Faça o run module de novo e teste a sua função lá
20. Faça o runTests
'''

'''import unittest
class TestStringMethods(unittest.TestCase):
    def test_01_quadrado(self):
        self.assertEqual(quadrado(2), 4)
        self.assertEqual(quadrado(-1), 1)
        self.assertEqual(quadrado(0), 0)
        self.assertEqual(quadrado(10), 100)
    def test_02_soma_dos_quadrados(self):
        self.assertEqual(soma_dos_quadrados(2,0), 4)
        self.assertEqual(soma_dos_quadrados(-1,1), 2)
        self.assertEqual(soma_dos_quadrados(0,0), 0)
        self.assertEqual(soma_dos_quadrados(10,20), 500)
def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)'''

'''
faça uma função que recebe uma lista de números e retorna a
soma de todos eles. NÃO utilize a função sum do python. Implemente a
lógica você mesmo!

def soma_de_lista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return soma
'''

'''
faça uma função que recebe uma lista de números e retorna a média.
ou seja, soma todos os números e divide pela quantidade de numeros

def media_da_lista(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    return '{:.2f}'.format(soma/len(lista))
'''

'''
faça uma função que acrescenta o proximo numero a uma lista.
por exemplo cresce([7,8]) deve devolver [7,8,9]

def cresce_lista(lista):
    ultimo = lista[-1]
    lista.append(ultimo+1)
    return lista
'''

'''
Explicacao
As próximas duas funções tem a ver com baralho.
A idéia é representar cada carta como uma string de 2 letras:
    as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
    os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus) 
O J de ouros, por exemplo, é representado pela string 'Jo'. O ás de copas,
pela string 'Ac'.
faça uma função que recebe um naipe de cartas ('o', que significa ouros,
'p', que significa paus, 'c' de copas ou 'e' de espadas) e retorna 
uma lista com todas as cartas desse naipe.
Entao, se você receber 'c', deve retornar deve retornar uma lista com 13 cartas, 
o ás de copas representado pela string 'Ac', os números '2c','3c',...'10c'
e as figuras,  'Jc', 'Qc', 'Kc'.
Dica: para juntar duas strings, faça nova='a'+'b'
Dica: para transformar um numero n em string, faça str(n)

def cria_naipe(naipe):
    cartas = ['4', '5', '6', '7', 'J', 'Q', 'K', 'A', '2', '3']
    lista_cartas = []
    for i in cartas:
        lista_cartas.append(i+naipe)
    return ' | '.join(lista_cartas)
'''

'''
faça uma função que cria um baralho completo, com todas as 52 cartas
ela nao recebe nada e retorna uma lista.
os naipes sao 'o' (ouros), 'c' (copas), 'e' (espadas) e 'p' (paus)
as cartas sao 'A' (ás) 2,3,4,5,...,10,'J','Q' e 'K'
O J de ouros, por exemplo, é representado pela string 'Jo'. 
Assim 'Jo' é um dos elementos que deve aparecer na lista

def cria_baralho():
    cartas = ['4', '5', '6', '7', 'J', 'Q', 'K', 'A', '2', '3']
    naipes = ['ouros', 'espada', 'copas', 'paus']
    baralho = []
    for carta in cartas:
        for naipe in naipes:
            carta_com_naipe = f'{carta} de {naipe.title()}'
            baralho.append(carta_com_naipe)
    return baralho

def cria_naipe(naipe):
    lista_final = []
    for i in cartas:
        lista_final.append(f'{i} de {naipe}')
    # return ' | '.join(lista_cartas)
    return lista_final
def cria_baralho():
    baralho = []
    for i in range(len(naipes)):
        # carta_com_naipe = f'{carta} de {naipe.title()}'
        carta_com_naipe = cria_naipe(naipes[i])
        baralho.extend(carta_com_naipe)
    return baralho
cartas = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
naipes = ['ouros', 'espada', 'copas', 'paus']
'''