# Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado

def ficha(nome='<Desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s)')

nomej = input('Nome: ').strip()
gols = input('Gol(s): ').strip()

gols = int(gols) if gols.isdigit() else 0

if nomej == '':
    ficha(gols=gols)
else:
    ficha(nomej,gols)