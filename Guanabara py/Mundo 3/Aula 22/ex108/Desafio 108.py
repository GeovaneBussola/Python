# Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.
import Moeda

numero = float(input('Digite um preço:R$'))
print(f'Aumentando o valor {Moeda.moeda(numero)} temos: {Moeda.moeda(Moeda.aumenta(numero,10))}')
print(f'Diminuindo o valor {Moeda.moeda(numero)} temos: {Moeda.moeda(Moeda.reduz(numero,20))}')
print(f'Dobrando o valor {Moeda.moeda(numero)} temos: {Moeda.moeda(Moeda.dobra(numero))}')
print(f'A metade de {Moeda.moeda(numero)} é: {Moeda.moeda(Moeda.metade(numero))}')