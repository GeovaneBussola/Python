# Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
media = 0
mulheresmenos20 = 0
homemmaisvelho = 0
nomehomemmaisvelho = ''
for i in range(1,5):
    print(f'{'-' * 7}{i}° Pessoa{'-'*7}')
    nome = input('Digite o nome da pessoa: ').strip()
    sexo = int(input('Digite o sexo\n[1] Masculino\n[2] Feminino\n'))
    idade = int(input('Digite a idade: '))
    if sexo == 1 and idade > homemmaisvelho:
        homemmaisvelho = idade
        nomehomemmaisvelho = nome
    if sexo == 2 and idade < 20:
        mulheresmenos20 += 1
    media += idade
media = media / 4
print(f'A media de idade do grupo é {media}, o homem mais velho do grupo é {nomehomemmaisvelho} e temos {mulheresmenos20} mulheres com menos de 20 anos no grupo')