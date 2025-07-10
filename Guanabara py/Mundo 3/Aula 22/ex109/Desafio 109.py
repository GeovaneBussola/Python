# Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.
import Moeda

numero = float(input('Digite um preço:R$'))
print(f'Aumentando o valor {Moeda.moeda(numero)} temos: {Moeda.aumenta(numero,10,True)}')
print(f'Diminuindo o valor {Moeda.moeda(numero)} temos: {Moeda.reduz(numero,20,True)}')
print(f'Dobrando o valor {Moeda.moeda(numero)} temos: {Moeda.dobra(numero,True)}')
print(f'A metade de {Moeda.moeda(numero)} é: {Moeda.metade(numero,True)}')