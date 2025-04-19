produto = input('Digite o nome do produto: ')
valorcompra = float(input('Digite o valor do produto: '))
if valorcompra < 10:
    valorcompra = valorcompra *1.7
elif valorcompra >= 10 and valorcompra <30:
    valorcompra = valorcompra *1.5
elif valorcompra >= 30 and valorcompra <50:
    valorcompra = valorcompra *1.4
else:
    valorcompra = valorcompra *1.3

print(f"O produto {produto} deve ser vendido por R${valorcompra:.2f}")