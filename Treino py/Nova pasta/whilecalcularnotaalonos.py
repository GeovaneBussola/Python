#Faça um algoritmo que calcula e mostra a média entre duas notas de 10 alunos. Use a
#estrutura de repetição enquanto
alunos = 1
mediatotal = 0
while alunos <11:
    nota1 = int(input('Digite sua primeira nota: '))
    nota2 = int(input('Digite sua segunda nota: '))
    media = (nota1 + nota2) /2
    print(f'A média do {alunos} é: {media}')
    alunos = alunos +1
    mediatotal = (mediatotal + media)
    mediatotalmax= mediatotal/10

print(f'A media total dos 10 alunos é: {mediatotalmax}')


