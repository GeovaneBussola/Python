#Temos um grupo de pessoas. Escreva um programa em Python que leia o sexo e a
#altura de cada pessoa, calcule e mostre a altura média das mulheres e dos homens
#separadamente. Utilize o comando de repetição que desejar
mulher=0
homem=0
mulheraltura=0
homemaltura=0
pessoas = int(input('Digite a quantidade de pessoas: '))
for i in range(1, pessoas + 1):
    pessoa = input(f'Digite o genero da {i} pessoa: ')
    pessoaltura = float(input('Digite a altura da pessoa: '))
    if pessoa == 'homem':
        homem+=1
        homemaltura+=pessoaltura
    elif pessoa == 'mulher':
        mulher+=1
        mulheraltura+=pessoaltura
    
print(f'Temos {mulher} mulheres, a media de altura delas é: {mulheraltura/mulher}')
print(f'Temos {homem} homens, a media de altura deles é: {homemaltura/homem}')

