palavra = input('Digite uma palavra: ').lower()
while " " in palavra:
    palavra = input('Digite apenas uma palavra: ').lower()
palavra_contrario = palavra[::-1]
if palavra == palavra_contrario:
    print('Esta palavra é palidromo')
else:
    print('Esta palavra não é palidromo')