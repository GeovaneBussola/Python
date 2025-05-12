faturamento = float(input('Digite o faturamento: '))
custo = float(input('Digite o custo: '))
lucro = faturamento - custo
lucro = f'R${lucro:_.2f}'
lucro = lucro.replace(',','.').replace('_','.')
print(f'O lucro foi de: {lucro}')