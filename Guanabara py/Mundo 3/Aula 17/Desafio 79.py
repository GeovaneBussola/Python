# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []

while True:
    num = int(input('Digite um numero para adicionar a lista: '))
    if num not in lista:
        print('Numero adicionado com sucesso!')
        lista.append(num)
    else:
        print('Numero não foi adicionado')
    while True:
        continuar = input('Deseja continuar [S/N]? ').lower().strip()
        if continuar not in ('n','s','não','nao','sim'):
            print('invalido!')
        else:
            break
    if continuar in ('n','não','nao'):
        break
print(f'Você digitou os valores: {sorted(lista)}')

        
        

    