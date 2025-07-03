# Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.
from random import randint
from time import sleep
def sorteia():
    lista=[]
    print('Sorteando os valores...')
    for i in range(5):
        lista.append(randint(1,10))
        print(f'{lista[i]} ',end='')
        sleep(0.2)
    print()
    return lista
def somapar(l):
    soma=0
    for i in l:
        if i %2 ==0:
            soma+=i
    print(f'Somando os valores pares de {l} temos: {soma}')
    
somapar(sorteia())

