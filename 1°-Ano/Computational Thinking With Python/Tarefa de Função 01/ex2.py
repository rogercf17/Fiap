linha = 40 * '='
def apresentacao_usuario(nome, idade, sexo, estado_civil):
    apresentacao = print(f'Dados do usuário\n{linha}\nNome: {nome}\nIdade: {idade}\nSexo: {sexo}\nEstado civíl: {estado_civil}')
    return apresentacao
apresentacao_usuario('Roger', 19, 'masculino', 'solteiro')
print()
apresentacao_usuario('Heitor', 12, 'masculino', 'solteiro')
print()
apresentacao_usuario('Rodrigo', 18, 'masculino', 'solteiro')
print()
apresentacao_usuario('Maria Vitória', 23, 'feminino', 'solteira')