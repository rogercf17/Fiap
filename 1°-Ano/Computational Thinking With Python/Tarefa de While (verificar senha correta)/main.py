'''
senha = input('Digite a senha para entrar: ')
senha_correta = '1234'
while senha != senha_correta:
    senha = input('Senha incorreta! Digite novamente: ')
print('Acesso liberado')
'''
senha = input('Digite a senha para entrar: ')
senha_correta = '1234'
t = 1
while senha != senha_correta and t < 3:
    senha = input('Digite a senha para entrar: ')
    t += 1
    if senha == senha_correta:
        print('Acesso liberado')
    else:
        print('Acesso negado')