# Exercício Python 097: Faça um programa que tenha uma função chamada escreva(), que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.                                  Ex:                                                                                                                                       escreva(‘Olá, Mundo!’)
#Saída:                                                           ~~~~~~~~~                                                                                                                                 Olá, Mundo!                                                                                                                            ~~~~~~~~~  

def escreva(texto):
    tamanho = len(texto) + 2
    print('~'*tamanho)
    print(f'{texto:^{tamanho}}')
    print('~'*tamanho)

mensagem=input('Digite: ')
escreva(mensagem)