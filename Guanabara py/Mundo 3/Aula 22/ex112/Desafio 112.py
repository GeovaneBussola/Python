# Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro pacote e mantenha tudo funcionando.
import Utilidades.moeda
import Utilidades.dado

numero = Utilidades.dado.leiadinheiro('Digite um valor: ')
Utilidades.moeda.resumo(numero,40,20)
