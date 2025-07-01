# Exercício Python 093: Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. Depois vai ler a quantidade de gols feitos em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.

jogador={'Gols':[]}
jogador['Nome'] = input('Digite o nome do Jogador: ')
jogador['Partida(s)'] = int(input(f'Digite a quantidade de partidas que o {jogador["Nome"]} jogou: '))
for i in range(jogador['Partida(s)']):
    jogador['Gols'].append(int(input(f'Digite quantos gols ele fez na {i+1}° partida: ')))
jogador['Total de gols']=sum(jogador["Gols"])
print(30*'-')
print(jogador)
print(30*'-')
print(f'O jogador {jogador["Nome"]} jogou {jogador["Partida(s)"]} partidas:')
for i in range(jogador['Partida(s)']):
    print(f'      >>>> {i+1}° partida fez {jogador["Gols"][i]} {"gol" if jogador["Gols"][i] == 1 else "gols"}')
print(f'O jogador fez {jogador["Total de gols"]} gol(s)')
    
