import string
texto = input('Digite um texto: ')
contador = 0
contador2 = 0
brakewhile= 1
lista = []
for i in string.punctuation:
        texto = texto.replace(i,"")
texto = texto.split()
contador = len(texto)
while contador != 0:
    for i in texto:
          brakewhile=1
          while brakewhile == 0:
                for a in texto:
                    if i > a:
                          contador2+=1
                    else:
                          lista.insert(contador2,i)
                          contador2= 0
                          brakewhile = 0

        

print(f'Este texto tem {contador} palavras, organizadas alfabeticamentes:{lista} ')