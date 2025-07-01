# xercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
jogadores = []
while True:
    jogador={'Gols':[]}
    jogador['Nome'] = input('Digite o nome do Jogador: ')
    jogador['Partida(s)'] = int(input(f'Digite a quantidade de partidas que o {jogador["Nome"]} jogou: '))
    for i in range(jogador['Partida(s)']):
        jogador['Gols'].append(int(input(f'Digite quantos gols ele fez na {i+1}° partida: ')))
    jogador['Total de gols']=sum(jogador["Gols"])
    jogadores.append(jogador.copy())
    while True:
        continua = input('Deseja adicionar mais alguem? (S/N)').upper().strip()
        if continua in ('S','N'):
            break
        else:
            print('Escolha apenas S ou N')
    if continua == 'N':
        break



    
