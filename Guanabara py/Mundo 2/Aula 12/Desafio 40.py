# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print(f'\033[31mSua média é {media} e voce esta reprovado\033[m')
elif media < 7:
    print(f'\033[33mSua média é {media} e você esta de recuperação\033[m')
else:
    print(f'\033[32mSua média é {media} e você esta aprovado\033[m') 