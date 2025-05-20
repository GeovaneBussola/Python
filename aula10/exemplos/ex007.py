# 7- Vamos criar um programa em Python que solicite ao usuário o nome de 5 pessoas,
# armazene em uma lista e exiba os nomes digitados e o tamanho da lista. Em seguida o
# programa deve solicitar ao usuário um nome, e o programa deverá remover o nome
# armazenado na lista, exibir os nomes digitados e o tamanho da lista.

nomes=[]
print('Digite 5 Nomes')
for i in range(5):
    nome=input(f'{i + 1}° Nome: ')
    nomes.append(nome)
while True:
    if len(nomes) == 0:
        print('A lista não possui nomes, Adeus!')
        break
    print(f'a lista pussui {len(nomes)} e os nomes da lista são: {", ".join(nomes)}')
    remover=input('Digite o nome que deseja remover ou [0 para sair]: ')
    
    if remover == "0":
        break
    elif remover in nomes:
        nomes.remove(remover)
    else:
        print('Nome inexistente na lista')
    
