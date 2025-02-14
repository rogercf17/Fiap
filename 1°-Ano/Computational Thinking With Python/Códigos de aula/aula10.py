
# TEORIA
#
# Um grafo é uma estrutura composta por pontos (vertices)
# e ligações entre pontos (arestas)
#
# Por exemplo, podemos ter uma rede social. Os vértices
# seriam pessoas, e as arestas seriam amizades entre pessoas
# 
# Ou poderiamos ter uma rede de computadores. No caso, os vértices seriam computadores, as arestas,
#  os cabos de rede
# 
# Ou poderiamos ter um mapa. Os vértices seriam cidades, as arestas, estradas ligando essas cidades.
#
# Exemplo:
#
# 0 - 2
# |   
# 1 - 3
#
# Esse grafo tem 4 vertices (0, 1, 2 e 3) e 3 arestas
# (uma ligação entre 0 e 1, que denotarei {0,1},
# uma entre 0 e 2 ({0,2}) e {1,3})
#
# Uma forma de representar grafos, que usaremos nesse arquivo
# é usando matrizes
#
# Para representar esse grafo, podemos usar a seguinte matriz
#
# 0110
# 1001
# 1000
# 0100
#
# Estamos usando 1 para representar a existencia de uma aresta, e 
# 0 para representar a inexistência.
#
# Por exemplo, se olharmos para a linha 0 e coluna 1 
# 0X10
# Y001
# 1000
# 0100
# (marcada com um X na matriz) vemos que há uma aresta entre 0 e 1
# a linha 1 coluna 0 (marcada com Y na matriz) diz o mesmo
#
# Se olharmos para a linha 2 coluna 3 (marcada com X)
# 0110
# 1001
# 100X
# 01Y0
# vemos que não há aresta entre 2 e 3
# (a linha 3 coluna 2, marcada com Y, diz o mesmo)
#
# Perceba que estamos contando do zero sempre
# 0110
# XXXX  -> linha 1 
# 1001
# 0100
#
#
# 01X0
# 10X0
# 10X1
# 01X0
#   |
#   --> coluna 2


# Vamos começar exercitando a leitura de um grafo nesse formato de matrizes
# 
# A pergunta que você vai ter que responder é:
# se estão ligados
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
# 
# Considerando o grafo
# 0000
# 0000
# 0001
# 0010
# 
# a resposta seria que os vertices 0 e 1 não estão ligados,
# como podemos ver tanto na posicao X quanto na posicao Y
# 0X00
# Y000
# 0001
# 0010
# Eu queria responder todos esses:
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
# Então a lista ficaria:
# exemplo = [False,False,False,False,False,True]

# Considerando o grafo
# 0100
# 1011
# 0101
# 0110
#
# diga, na lista arestas_1, se estão ligados
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
#
# crie uma lista como no exemplo
arestas_1 = []

# Considerando o grafo
# 0111
# 1001
# 1000ma
# 1100
#
# diga, na lista arestas_2, se estão ligados
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
#
# crie uma lista como no exemplo
arestas_2 = []

# Considerando o grafo
# 0001
# 0010
# 0100
# 1000
#
# diga, na lista arestas_3, se estão ligados
# 0 e 1, 0 e 2, 0 e 3, 1 e 2, 1 e 3, 3 e 2
#
# crie uma lista como no exemplo:
arestas_3 = []

# Alias, qual o máximo de arestas que um grafo com
# 2 vértices pode ter? e com 3? e com 4? e com 5? e com 6?
#
# coloque suas respostas em uma lista max_arestas como no exemplo max_arestas = [0,0,-1,3,4] (mas preenchendo
# os números corretos)
max_arestas = []

# Escreva uma funcao que recebe um grafo,
# representado por uma matriz, a quantidade de vertices, e dois vertices,
# v1 e v2, e devolve True se existe aresta entre eles.

def existe_aresta(matriz_adjacencia, num_vertices, v1, v2):
    if v1 < 0 or v1 >= num_vertices or v2 < 0 or v2 >= num_vertices:
        return False
    return matriz_adjacencia[v1][v2] != 0




# Escreva uma funcao que recebe um grafo,
# representado por uma matriz, a quantidade de vertices, e dois vertices,
# v1 e v2, e altera o grafo para que haja arestas entre os vertices

def adiciona_aresta(arestas, num_vertices, v1, v2):
    pass 


# faca o mesmo, agora para remover arestas, em uma funcao remove_aresta
def remove_aresta(arestas, num_vertices, v1, v2):
    pass



# faca uma funcao conta_arestas, que conta o numero de arestas
# de um grafo.
def conta_arestas(arestas, num_vertices):
    pass



# direi que um grafo eh uma "estrela", ou ainda um "asterisco"
# se todos existe um vertice "central", conectado a todos os
# demais, e todo vertice nao central so tem uma aresta: aquela
# que vai para o central.
#
# ex:
#        2
#        |
#    0 - 3 - 1
#        |
#        4
# Esse grafo eh uma estrela com vertice central 3
#
# Crie uma funcao eh_estrela, que recebe o grafo e seu numero 
# de vertices
def eh_estrela(arestas, num_vertices):
    pass




# Crie uma função que recebe a matriz que representa
# um grafo, o numero de vertices e o numero de um
# vertice V específico. 
# Ela retorna uma lista com todos os vertices vizinhos de 
# V
def vizinhos(arestas, num_vertices, V):
    pass

# Crie uma função que recebe a matriz que representa
# um grafo, o numero de vertices e o numero de um
# vertice V específico. 
# Retorna uma lista com todos os números dos vizinhos
# de V, mas também os vizinhos de vizinhos. 
#
# Nao coloque vizinho de vizinho de vizinho
#
# Cuidado para não repetir vertices, e pra não colocar o proprio V na lista
#
def mais_vizinhos(arestas, num_vertices, V):
    pass

# agora faca uma funcao todos os vizinhos, que inclui vizinhos imediatos,
# "de segundo grau", "de terceiro grau" e assim ate o fim do grafo

# Pode ser útil manter uma lista de pendencias, uma lista de vizinhos
# que você já descobriu (já achou) mas ainda não 'visitou' (ainda não pensou)
# nos vizinhos deles

def todos_os_vizinhos(arestas, num_vertices, V):
   pass


# A partir daqui, soh codigo de testes/utilitario
# Nada para voce fazer

gr1 = [[0,1,0,0,0,1],      #     1 - 2
       [1,0,1,0,0,0],      #    /    | 
       [0,1,0,1,0,0],      #   0     3 
       [0,0,1,0,1,0],      #    \    |
       [0,0,0,1,0,1],      #     5 - 4
       [1,0,0,0,1,0]]

gr2 = [[0,1,0,0,0,1],       # ----------------
       [1,0,0,0,0,1],       # |    1    2    |
       [0,0,0,1,1,0],       # |   /|    |\   |
       [0,0,1,0,1,0],       # |  0 |    3 |  |
       [0,0,1,1,0,0],       # |   \|    |/   |
       [1,1,0,0,0,0]];      # |    5    4    |
                            # ----------------

gr3 = [[0,1,0,1,0,1],       # ----------------
       [1,0,0,0,0,1],       # |    1    2    |
       [0,0,0,1,1,0],       # |   /|    |\   |
       [1,0,1,0,1,0],       # |  0----- 3 |  |
       [0,0,1,1,0,0],       # |   \|    |/   |
       [1,1,0,0,0,0]]       # |    5    4    |
                            # ----------------

gr4 = [[0,1,1,1,1,1],       # ------------------
       [1,0,0,0,0,0],       # |  1 2  estrela! |
       [1,0,0,0,0,0],       # |  |/            |
       [1,0,0,0,0,0],       # |  0--3          |
       [1,0,0,0,0,0],       # |  |\            |
       [1,0,0,0,0,0]]       # |  5 4           |
                            # ------------------

gr5 = [[0,0,1,0,0,0],       # ------------------
       [0,0,1,0,0,0],       # |  1 0  estrela! |
       [1,1,0,1,1,1],       # |  |/            |
       [0,0,1,0,0,0],       # |  2--3          |
       [0,0,1,0,0,0],       # |  |\            |
       [0,0,1,0,0,0]];      # |  5 4           |
                            # ------------------

gr6 = [[0,0,1],     #
       [0,0,1],     #  0 - 2 - 1
       [1,1,0]]     #
                    #  (eh estrela?)
       
gr7 = [[0,0,1,0,0,0],    # ------------------
       [0,0,1,0,0,0],    # |  1       4     |
       [1,1,0,0,0,0],    # |  |       |     |
       [0,0,0,0,1,1],    # |  2       3     |
       [0,0,0,1,0,0],    # |  |       |     |
       [0,0,0,1,0,0]]    # |  0       5     |
                         # ------------------


# clean: ideias: uma função que retorna um dicionario vertice-distancia
# clean: ideias: ver o video e achar mais exemplos simples


import unittest
import hashlib

def verifica_lista_b(lista, tamanho, soma_esperada):
    potencia = 1
    soma = 0
    for i in range(tamanho):
        soma += lista[i] * potencia
        potencia *= 2
    if soma == soma_esperada:
        return True
    raise ValueError("A lista passada nao correspondeu a lista esperada")



class TestStringMethods(unittest.TestCase):

   def test01a_listas_true_false(self):
      self.assertEqual(len(arestas_1),6)
      verifica_lista_b(arestas_1,6,57)
'''
   def test01b_listas_true_false(self):
       self.assertEqual(len(arestas_2),6)
       verifica_lista_b(arestas_2,6,39)
'''

    def test01c_listas_true_false(self):
       self.assertEqual(len(arestas_3),6)
       verifica_lista_b(arestas_3,6,12)


   def test02_lista_tamanhos(self):
       self.assertEqual(len(max_arestas),5)
       verifica_lista_b(max_arestas,5,351)
   

   def test03a_existe_aresta(self):
    self.assertTrue(existe_aresta(gr1,6,0,1))
    self.assertFalse(existe_aresta(gr1,6,0,2))
    self.assertTrue(existe_aresta(gr1,6,1,2))
    self.assertTrue(existe_aresta(gr1,6,5,4))
    self.assertFalse(existe_aresta(gr1,6,1,4))
    self.assertFalse(existe_aresta(gr1,6,1,5))
    self.assertFalse(existe_aresta(gr1,6,2,4))

   def test03b_existe_aresta(self):
    self.assertTrue(existe_aresta(gr2,6,0,1))
    self.assertFalse(existe_aresta(gr2,6,0,2))
    self.assertFalse(existe_aresta(gr2,6,1,2))
    self.assertFalse(existe_aresta(gr2,6,5,4))
    self.assertFalse(existe_aresta(gr2,6,1,4))
    self.assertTrue(existe_aresta(gr2,6,1,5))
    self.assertTrue(existe_aresta(gr2,6,2,4))
    self.assertFalse(existe_aresta(gr2,6,0,3))
    self.assertTrue(existe_aresta(gr3,6,0,3))

   def test04a_adiciona_aresta(self):
    self.assertFalse(existe_aresta(gr3,6,1,2))
    adiciona_aresta(gr3,6,1,2)
    self.assertTrue(existe_aresta(gr3,6,1,2))
    self.assertTrue(existe_aresta(gr3,6,2,1))
   
   def test04b_adiciona_aresta(self):
   
    self.assertFalse(existe_aresta(gr3,6,5,4))
    adiciona_aresta(gr3,6,5,4)
    self.assertTrue(existe_aresta(gr3,6,5,4))
    self.assertTrue(existe_aresta(gr3,6,4,5))

   def test05_remove_aresta(self):
    remove_aresta(gr3,6,5,4)
    remove_aresta(gr3,6,1,2)
    self.assertFalse(existe_aresta(gr3,6,5,4))
    self.assertFalse(existe_aresta(gr3,6,4,5))
    self.assertFalse(existe_aresta(gr3,6,1,2))
    self.assertFalse(existe_aresta(gr3,6,2,1))
    remove_aresta(gr1,6,0,1)
    self.assertFalse(existe_aresta(gr1,6,0,1))
    self.assertFalse(existe_aresta(gr1,6,1,0))
    adiciona_aresta(gr1,6,0,1)
    self.assertTrue(existe_aresta(gr1,6,0,1))
    self.assertTrue(existe_aresta(gr1,6,1,0))

   def test06_conta_arestas(self):
    self.assertEqual(conta_arestas(gr1,6),6)
    self.assertEqual(conta_arestas(gr2,6),6)
    self.assertEqual(conta_arestas(gr3,6),7)
    self.assertEqual(conta_arestas(gr4,6),5)
    self.assertEqual(conta_arestas(gr5,6),5)
    self.assertEqual(conta_arestas(gr6,3),2)

   def test07_eh_estrela(self):
    self.assertFalse(eh_estrela(gr1,6))
    self.assertFalse(eh_estrela(gr2,6))
    self.assertFalse(eh_estrela(gr3,6))
    self.assertTrue(eh_estrela(gr4,6))
    self.assertTrue(eh_estrela(gr5,6))
    self.assertTrue(eh_estrela(gr6,3))

   def test08a_vizinhos(self):
       self.assertEqual(len(vizinhos(gr1,6,1)),2)
       self.assertIn(0,vizinhos(gr1,6,1)) # 0 tem que ser elemento dessa lista
       self.assertIn(2,vizinhos(gr1,6,1)) # 2 tem que ser elemento dessa lista


   def test08b_vizinhos(self):
       self.assertEqual(len(vizinhos(gr3,6,0)),3)
       self.assertIn(1,vizinhos(gr3,6,0)) # 1 tem que ser elemento dessa lista
       self.assertIn(5,vizinhos(gr3,6,0)) # 5 tem que ser elemento dessa lista
       self.assertIn(3,vizinhos(gr3,6,0)) # 3 tem que ser elemento dessa lista

   def test09a_mais_vizinhos(self):
       self.assertEqual(len(mais_vizinhos(gr1,6,1)),4)
       
       self.assertIn(0,mais_vizinhos(gr1,6,1))
       self.assertIn(5,mais_vizinhos(gr1,6,1))
       self.assertIn(3,mais_vizinhos(gr1,6,1))
       self.assertIn(2,mais_vizinhos(gr1,6,1))

   def test09b_mais_vizinhos(self):
       self.assertEqual(len(mais_vizinhos(gr7,6,2)),2)
       self.assertIn(0,mais_vizinhos(gr7,6,2))
       self.assertIn(1,mais_vizinhos(gr7,6,2))

       self.assertEqual(len(mais_vizinhos(gr7,6,1)),2)
       self.assertIn(0,mais_vizinhos(gr7,6,1))
       self.assertIn(2,mais_vizinhos(gr7,6,1))

       self.assertEqual(len(mais_vizinhos(gr7,6,5)),2)
       self.assertIn(3,mais_vizinhos(gr7,6,5))
       self.assertIn(4,mais_vizinhos(gr7,6,5))
       
   def test10a_todos_os_vizinhos(self):
    self.assertEqual(len(todos_os_vizinhos(gr1,6,1)),5)
    self.assertIn(0,todos_os_vizinhos(gr1,6,1))
    self.assertIn(5,todos_os_vizinhos(gr1,6,1))
    self.assertIn(3,todos_os_vizinhos(gr1,6,1))
    self.assertIn(2,todos_os_vizinhos(gr1,6,1))
    self.assertIn(4,todos_os_vizinhos(gr1,6,1))

   def test10b_todos_os_vizinhos(self):
    self.assertEqual(len(todos_os_vizinhos(gr7,6,2)),2)

    self.assertIn(0,todos_os_vizinhos(gr7,6,2))
    self.assertIn(1,todos_os_vizinhos(gr7,6,2))

    self.assertEqual(len(todos_os_vizinhos(gr7,6,1)),2)
    self.assertIn(0,todos_os_vizinhos(gr7,6,1))
    self.assertIn(2,todos_os_vizinhos(gr7,6,1))

    self.assertEqual(len(todos_os_vizinhos(gr7,6,5)),2)
    self.assertIn(3,todos_os_vizinhos(gr7,6,5))
    self.assertIn(4,todos_os_vizinhos(gr7,6,5))


try: 
   from intro_grafos_gabarito import *
except:
   pass

def runTests():
        suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestStringMethods)
        unittest.TextTestRunner(verbosity=2,failfast=True).run(suite)

# runTests()

# import numpy as np
# import math

# matriz = np.arange(15, dtype=np.int64)
# print(matriz)
# matriz = matriz.reshape(5,3)
# print(matriz)

# matriz[1:, ::2] = -1
# print(matriz)

# maximo = matriz.max(axis=1)
# print(maximo)

# print(matriz.shape) (N° de linhas, N° de colunas)
# print(matriz.size) Número de elementos
# print(matriz.ndim) Número de dimensões largura e altura

# if matriz.size == math.prod(matriz.shape):
#     print('Verdadeiro')

# print(np.zeros(2, dtype=np.int64))
# print(np.ones(2))
# print(np.empty(5))
# print(np.arange(5, 20, 2))
# print(np.linspace(0, 10, 5, dtype=np.int64))


