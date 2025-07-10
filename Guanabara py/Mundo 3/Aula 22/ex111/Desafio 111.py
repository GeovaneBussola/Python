# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
import Utilidades.moeda

numero = float(input('Digite um preço:R$'))
Utilidades.moeda.resumo(numero,40,20)
