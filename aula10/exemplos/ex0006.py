# 6- Faça um programa em Python que leia o nome e duas notas de n alunos e calcule a
# média. O usuário deverá digitar o número do aluno e o programa exibirá a média e o
# resultado, sabendo que o critério para aprovação é média igual ou maior que 6.0.
nomes=[]
medias=[]
resultados=[]
while True:
    nome= input('Digite o nome do aluno: ')
    n1= float(input('Digite a nota 1 do aluno: '))
    n2= float(input('Digite a nota 2 do aluno: '))
    media = (n1 + n2) / 2
    estado = 'Aprovado' if media >= 6 else "Reprovado"
    resultados.append(estado)
    nomes.append(nome)
    medias.append(media)
    print('Alunos cadastrados:')
    for aa,ab in enumerate(nomes):
        print(f'[{aa + 1}] {ab}')

    a = int(input('Digite [1] para continuar ou [2] para parar: '))
    if a == 2:
        break
while True:
    numeroaluno=int(input('Digite o numero do aluno para verirfizar seu resultado (0 para sair): '))
    if 1 <= numeroaluno <= len(nomes):
        print(f'Aluno(a) Numero {numeroaluno}({nomes[numeroaluno -1]})\nMédia: {medias[numeroaluno -1]}\nResultado: {resultados[numeroaluno -1]}')
    elif numeroaluno == 0:
        break
    else:
        print('Numero invalido')
        


    

