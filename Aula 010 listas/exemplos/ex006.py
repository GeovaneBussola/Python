# 6- Faça um programa em Python que leia o nome e duas notas de n alunos e calcule a
# média. O usuário deverá digitar o número do aluno e o programa exibirá a média e o
# resultado, sabendo que o critério para aprovação é média igual ou maior que 6.0.
nomes=[]
medias=[]
resultados=[]
while True:
    while True:
        nome= input('Digite o nome do aluno ou (0 para sair): ')
        if nome != "0":
            nomes.append(nome)
        else:
            break
    for i in nomes:
        n1= float(input(f'Digite a nota 1 do(a) {i}: '))
        n2= float(input(f'Digite a nota 2 do(a) {i}: '))
        media = (n1 + n2) / 2
        estado = 'Aprovado' if media >= 6 else "Reprovado"
        resultados.append(estado)
        medias.append(media)
    print('Alunos cadastrados:')
    for aa,ab in enumerate(nomes):
        print(f'[{aa + 1}] {ab}')
    break
while True:
    numeroaluno=int(input('Digite o numero do aluno para verirfizar seu resultado (0 para sair): '))
    if 1 <= numeroaluno <= len(nomes):
        print(f'Aluno(a) [{nomes[numeroaluno -1]}]\nMédia: {medias[numeroaluno -1]}\nResultado: {resultados[numeroaluno -1]}')
    elif numeroaluno == 0:
        break
    else:
        print('Numero invalido')
        


    

