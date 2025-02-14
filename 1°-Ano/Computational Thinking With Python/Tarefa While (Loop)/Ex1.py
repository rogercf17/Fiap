nota = int(input('Digite uma nota entre 1 e 10: '))
while nota < 1 or nota > 10:
    print('Nota inválida, tente novamente!')
    nota = int(input('Digite uma nota entre 1 e 10: '))
print(f'Ok nota digita é {nota}.')