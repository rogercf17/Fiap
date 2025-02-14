qntd_macas = int(input('Digite a quantidade de maçãs compradas: '))
preco_maca = 0

if qntd_macas >= 12:
    preco_maca = 0.25
else:
    preco_maca = 0.30
    
valor_da_compra = preco_maca * qntd_macas
print(f'Você comprou {qntd_macas} maçãs e o valor da compra ficou de R$ {valor_da_compra}')