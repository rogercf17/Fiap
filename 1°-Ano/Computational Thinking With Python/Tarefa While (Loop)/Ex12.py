i = 0
soma = 0
qntd = int(input('Quantas notas serão digitadas? '))
while i < qntd:
    nota = int(input(f'Digite a {i+1}ª nota: '))
    soma += nota
    i += 1
print(f'A médias das {qntd} notas é {soma/qntd}')