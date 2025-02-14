lista_de_carros = ['Uno', 'Corsa', 'Hb20', 'Gol', 'Sandero']
lista_preco_carros = [48, 29, 85, 54, 68]
def verifica_maior_preco(lista1, lista2):
    maior_preco = lista_preco_carros[0]
    carro = lista_de_carros[0]
    for c in range(len(lista1)):
        if lista1[c] > maior_preco:
            maior_preco = lista1[c]
            carro = lista2[c]
    return print(f'O {carro} é o carro mais caro da lista, custando {maior_preco} mil reais.')
verifica_maior_preco(lista_preco_carros, lista_de_carros)