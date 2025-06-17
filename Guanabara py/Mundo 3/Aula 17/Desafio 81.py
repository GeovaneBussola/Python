# Exercício Python 081: Crie um programa que vai ler vários números e colocar em uma lista. Depois disso mostre:                                                                                                                                   # A) Quantos números foram digitados.
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista.
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
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} numeros')
print(f'Organizados de forma decrescente: {lista}')
print(f'O valor 5 foi digitado {lista.count(5)} veze(s) na lista') if 5 in lista else print('O valor 5 nao foi digitado, portanto não esta na lista')
