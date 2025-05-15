# 2- Vamos criar um programa em Python que solicite ao usuário o nomes de 5 pessoas e
# armazene em uma lista.
# Em seguida o programa deve solicitar ao usuário um número de 0 a 4, correspondendo
# ao índice, e o programa deverá mostrar nome armazenado nesse índice.
nomes=[]
for i in range(1,6):
    nome = input(f'Digite o {i} nome: ')
    nomes.append(nome)
while True: 
    indice=input('Digite o indice do nome que gostaria de ver: ')
    if not indice.isdigit():
        print(f'O indice deve ser um numero "(1-{len(nomes)})"')
        continue
    indice = int(indice)
    if indice <=0 or indice > len(nomes):
        print(f'Indice inexistente, por favor digite um valor valido "(1-{len(nomes)})"')
        continue
    break
print(f'O nome no indice {indice} é {nomes[indice-1]}')