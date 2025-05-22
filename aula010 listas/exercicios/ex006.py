# 6- Faça um programa em Python que solicite ao usuário, enquanto o mesmo desejar,
# números e armazene-os em uma lista.
# Após a entrada de dados, somar os valores da lista, calcular e mostrar a média.
# Calcule e mostre quantos números armazenados na lista estão acima da média.

lista=[]
numeros_acima_media=0
print('Digite quantos numeros desejar ou [x] para parar')
while True:
    numero=(input())
    if numero == "x":
        break
    else:
        lista.append(float(numero))
media = sum(lista) / len(lista)
for i in lista:
    if i > media:
        numeros_acima_media+=1
print(f'Média: {media:.1f}')
print(f'Numeros acima da média: {numeros_acima_media}')
        
    
