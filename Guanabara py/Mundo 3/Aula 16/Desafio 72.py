# Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida com uma contagem por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

numeros = 'zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezeseis','dezesete','dezoito','dezenove','vinte'
while True:
    num = int(input('Digite um numero inteiro entre 0 e 20: '))
    if num >20 or num <0:
        print('Tente novamente. ', end='')
    else:break 
print(f'Você digitou o numero {numeros[num]}')