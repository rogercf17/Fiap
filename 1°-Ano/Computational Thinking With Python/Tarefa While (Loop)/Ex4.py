c = 0
soma = 0
while c < 5:
    num = input(f'Digite o {c+1}° número: ')
    while not num.isnumeric():
        print('Deve ser um número!')
        num = input(f'Digite o {c+1}° número: ')
    num = int(num)
    soma += num
    c += 1
print(f'a soma dos número digitados é igual a {soma} e a media é {soma/c}')