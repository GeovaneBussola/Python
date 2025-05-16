# 5- Vamos fazer um programa em Python que controle a utilização de 5 salas do cinema
# CINEMARKO. O programa deverá ter as seguintes funcionalidades:
# ▪ Uma lista deverá armazenar os lugares vagos por sala: lugaresVagos = [10, 5, 6, 8, 0],
# respectivamente para as sala 1, 2, 3, 4 e 5.
# ▪ O usuário deverá digitar o número da sala e a quantidade de ingressos que deseja
# comprar, ou zero para encerrar o programa.
# ▪ O programa deverá verificar se a venda é possível antes de concretizá-la, informando
# quando não há lugares disponíveis para venda.
# ▪ Caso a compra seja efetivada, atualizar o número de lugares livres e exibir na tela.

salas=[10, 5, 6, 8, 0]
while True:
    sala = int(input('Digite a sala na qual deseja comprar ingreso(s): '))
    if salas[sala -1] == 0:
        print('Desculpe mas esta sala ja esta cheia, escolha outra sala')
        continue
    while True:
        compra = input(f'Digite quantos ingressos deseja comprar: ')
        if salas[sala -1] < compra:
            print(f'Esta sala possui apenas {salas[sala-1]} ingressos')
        else:
            

    

