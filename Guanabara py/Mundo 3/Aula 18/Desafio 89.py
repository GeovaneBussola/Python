# Exercício Python 089: Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
lista=[]
contador=0
while True:
    nome = input('Digite o nome: ')
    n1 = float(input('Digite a n1 do aluno: '))
    n2 = float(input('Digite a n2 do aluno: '))
    lista.append(list())
    lista[contador].append(nome)
    lista[contador].append([n1,n2])
    contador+=1
    if input('Deseja adicionar mais algum aluno? [s/n] ').lower().strip() in ('não','nao','n'):
        break

print('=-'*15)
print('Num   Nome      Média')
print('-'*24)
for i in range(len(lista)):
    print(f'{i}     {lista[i][0]:<12}{(lista[i][1][0] + lista[i][1][1]) / 2}')
print('=-'*15)
while True:
    nota=int(input('Mostrar nota de qual aluno? [999] para interromper'))
    if nota == 999:
        break
    elif lista[nota] in lista:
        print('tem')
    else:
        print('nao tem')