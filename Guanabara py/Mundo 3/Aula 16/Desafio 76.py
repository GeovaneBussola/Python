# Exercício Python 076: Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista=('Abacate',3,'Limão',1,'Mexirica',3,'Abacaxi',8,'Mamão', 700)
print('-' * 30)
print('{:^30}'.format('LISTA DE PREÇOS'))
print('-' * 30)
contador =0
for i in lista:
    if contador == 0:
        print('{:.<20}R$'.format(i), end='')
        contador = 1
    else:
        print('{:>7.2f}'.format(i))
        contador= 0

print('-' * 30)