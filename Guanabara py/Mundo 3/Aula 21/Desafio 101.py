# Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
def voto(ano):
    from datetime import date
    idade = date.today().year - ano
    print(f'Com {idade} anos de idade: ',end='')
    if idade < 16:
        print('Não vota')
    elif 16 <= idade <= 17 or idade > 65:
        print('Voto opcional')
    else:
        print('Vota')
    
    
anonascimento = int(input('Digite o ano do nascimento: '))
voto(anonascimento)