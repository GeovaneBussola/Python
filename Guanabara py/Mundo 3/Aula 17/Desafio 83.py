# Exercício Python 083: Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

contador = 0
invalido = 0
expressão = str(input('Digite sua expressão: '))
for i in expressão:
    if i == ')':
        contador -=1
    elif i == '(':
        contador+=1
    if contador < 0:
        invalido = 1
        break
if contador == 0 and invalido == 0:
    print('Sua expressão é valida')
else:
    print('Sua expressão é invalida')

