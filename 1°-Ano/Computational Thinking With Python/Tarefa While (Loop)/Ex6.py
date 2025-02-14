nome_usuario = input('Digite seu nome de usuário: ')
senha = input('Digite sua senha: ')
while nome_usuario == senha:
    print('Nome de usuário e senha iguais, digite novamente!')
    nome_usuario = input('Digite seu nome de usuário: ')
    senha = input('Digite sua senha: ')
print('Acesso liberado!')