# 4- Faça um programa em Python que solicite ao usuário o dia da semana e o volume de
# chuva correspondente a 10 dias. As informações obtidas devem ser armazenadas em 2
# listas distintas (observe que cada lista poderá ter apenas 10 itens armazenados e que na
# posição i das duas listas ficarão armazenados: o dia da semana i e o volume de chuva i). É
# obrigatório o uso de estrutura de repetição e listas.
# Em seguida, calcule e mostre o volume médio de chuva apenas do dia de semana igual a
# quarta-feira e a soma total do volume de chuva, para isso utilize os dados armazenados
# nas listas. É obrigatório o uso de estrutura de repetição e das listas do exercício descritas
# anteriormente.

dias=[]
volumes=[]
media=0
contador=0
print('Digite o dia da semana e o volume de chuva do dia:')
for i in range(1,11):
    dias.append(input(f'{i}° dia: ').lower())
    volumes.append(float(input('Volume: ')))
for i,a in enumerate(dias):
    if a == 'quarta' or a == 'quarta-feira':
        media+= volumes[i]
        contador+=1
media = media / contador
print(f'A media de volume de chuva da quarta-feira é {media:.2f}\nA soma total do volume de chuva é {sum(volumes)}')




