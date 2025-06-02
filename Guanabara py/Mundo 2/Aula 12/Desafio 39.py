# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Digite seu ano de nascimento: '))
ano = date.today().year - ano
if ano > 18:
    print(f'Já passou o tempo do alistamento, ja se passaram {ano - 18} ano(s)')
elif ano == 18:
    print('Voce esta no momento de se alistar')
else:
    print(f'Voce deve se alistar daqui a {18 - ano} ano(s)')
