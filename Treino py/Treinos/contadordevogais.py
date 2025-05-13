#Contador de vogais
vogais= ["aeiou"]
texto = input('Digite um texto: ').lower()
nvogais = 0
for i in vogais:
    qvogais = texto.count(i)
    nvogais += qvogais

print(f'Temos {nvogais} vogais neste texto')