# xercício Python 095: Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.


#lista dos dados
jogadores = []


# Entrada de dados
while True:
    jogador={'Gols':[]}
    jogador['Nome'] = input('Digite o nome do Jogador: ').capitalize()
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
print('-='*18)
a =(f'{"Num":^6}{"Jogador":<15}{"Total":<8}{"Gols"}')
print(a)
print((len(a) + 2)*"-")


#Analisar dado especifico
for i, v in enumerate(jogadores):
    print(f'{i:^5} {v["Nome"]:<15}{v["Total de gols"]:^8}{v["Gols"]}')
print((len(a) + 2)*"-")
while True:
    acessar = int(input('Deseja fazer o levantamento de qual jogador? '))
    if acessar == 999:
        break
    elif acessar < 0 or acessar >= len(jogadores):
        print('Digite um codigo valido!')
        continue
    print(f'-- Levantamento do Jogador {jogadores[acessar]["Nome"]}:')
    for i in range(len(jogadores[acessar]['Gols'])):
        print(f'Na {i+1}° partida fez {jogadores[acessar]["Gols"][i]}')
    


    
