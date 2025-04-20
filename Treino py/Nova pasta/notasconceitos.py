# Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina
# ao longo de um semestre, e calcule a sua média. A atribuição de conceitos obedece à
# tabela:
# O programa deverá mostrar na tela o conceito correspondente e a mensagem
# “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for D ou E.

n1 = float(input("Digite sua primeira nota: "))
n2 = float(input("Digite sua segunda nota: "))
media = (n1+n2) / 2
if media < 4:
    print('Voce foi reprovado. Seu conceito é E')
elif media >= 4 and media <= 5.9:
    print('Voce foi reprovado. Seu conceito é D')
elif media >= 6 and media <= 7.4:
    print('Voce foi aprovado. Seu conceito é C')
elif media >= 7.5 and media <= 8.9:
    print('Voce foi aprovado. Seu conceito é B')
elif media >= 9 and media <=10:
    print('Voce foi aprovado. Seu conceito é A')