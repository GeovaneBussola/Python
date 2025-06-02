# Exercício Python 041: A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# – Até 9 anos: MIRIM
# – Até 14 anos: INFANTIL
# – Até 19 anos: JÚNIOR
# – Até 25 anos: SÊNIOR
# – Acima de 25 anos: MASTER

from datetime import date

data = date.today().year
ano_atleta = data - int(input('Digite o ano do seu nascimento: '))
if ano_atleta < 10:
    print('Mirim')
elif ano_atleta < 15:
    print('Infantil')
elif ano_atleta < 20:
    print('Júnior')
elif ano_atleta < 26:
    print('Sênior')
else:
    print('Master')

