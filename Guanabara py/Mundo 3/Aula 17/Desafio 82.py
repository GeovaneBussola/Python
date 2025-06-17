# Exercício Python 082: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o conteúdo das três listas geradas.

lista=[]
while True:
    vl = input('Digite um valor ou x para sair').lower().strip()
    try:
        vl = int(vl)
        lista.append(vl)
    except ValueError:
        if vl == 'x':
            break
        else:
            print('Digito invalido')
            continue
impares = []
pares = []

for i in lista:
    if i != 0:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
print(f'lista digitada: {lista}')
print(f'Lista de pares: {pares}')
print(f'Lista de impares: {impares}')