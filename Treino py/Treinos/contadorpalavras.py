#Contador de palavras
import string
texto = input('Digite um texto: ')
contador = 0
for i in string.punctuation:
        texto = texto.replace(i,"")
texto = texto.split()
contador = len(texto)

print(f'Este texto tem {contador} palavras')