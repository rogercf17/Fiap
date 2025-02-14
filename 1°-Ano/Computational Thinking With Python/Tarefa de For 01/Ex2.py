soma = 0
for i in range(10):
    num = int(input(f'Digite o {10-i}° número: '))
    soma += num
print(f'Soma dos números = {soma}\nMédias dos números = {soma/10}')