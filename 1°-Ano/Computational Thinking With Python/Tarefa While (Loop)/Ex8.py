i = 1
c = 1
contador = 3
print(i, end=' ')
print(c, end=' ')
while contador <= 9:
    aux = i + c
    print(aux, end=' ')
    i = c
    c = aux
    contador += 1
print(f'\nFim esses são os 9 primeiros termos da sequência de fibonacci.')