# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista=[]
contador=0
while True:
    nome = input('Digite o nome: ').capitalize()
    n1 = float(input('Digite a n1 do aluno: '))
    n2 = float(input('Digite a n2 do aluno: '))
    lista.append(list())
    lista[contador].append(nome)
    lista[contador].append([n1,n2])
    contador+=1
    if input('Deseja adicionar mais algum aluno? [s/n] ').lower().strip() in ('não','nao','n'):
        break

print('=-'*15)
print(f'{"Num":<4}{"Nome":<10}{"Média":<8}')
print('-'*24)
for i in range(len(lista)):
    print(f'{i:<4}{lista[i][0]:<10}{(lista[i][1][0] + lista[i][1][1]) / 2:<7.1f}')
print('=-'*15)
while True:
    nota=int(input('Mostrar nota de qual aluno? [999] para interromper'))
    print('-'*24)
    if nota == 999:
        break
    elif 0 <= nota < len(lista):
        print(f'A nota do(a) aluno é: {lista[nota][1]}')
        print('-'*24)
    else:
        print('posição inexistente')
        print('-'*24)