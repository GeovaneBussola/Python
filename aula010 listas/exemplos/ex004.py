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
def comprar_ingressos():
    while True:
        print('Salas:')
        for ab,ac in enumerate(salas):
            print(f'Sala {ab + 1}: [{ac}] ingresos')
            
        chave =1
        sala = int(input('Digite a sala na qual deseja comprar ingreso(s): '))
        if sala >5 or sala <1:
            print('Sala inexistente')
            continue
        elif salas[sala -1] == 0:
            print('Esta sala ja esta cheia, escolha outra sala')
            continue
        
        while chave ==1:
            compra = int(input(f'Digite quantos ingressos deseja comprar: '))
            if salas[sala -1] < compra:
                print(f'Esta sala possui apenas {salas[sala-1]} ingressos')
                chave = int(input('Digite "0" para trocar de sala \nDigite "1" para mudar a quantidade de ingresos que deseja comprar\n '))
                if chave == 0:
                    break
                if chave == 1:
                    continue
            else:
                salas[sala -1] -= compra
                print(f'{salas}')
                chave = int(input(f'Digite\n"0" Para comprar mais ingresos ou "1" para encerrar'))
                if chave == 0:
                    break
                elif chave == 1:
                    print('Obrigado pela compra!! volte sempre :)')
                    return
comprar_ingressos()


            
        

        

        
            

    

