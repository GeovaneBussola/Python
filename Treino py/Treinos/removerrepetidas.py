palavra = input('Digite uma palavra: ').lower().lstrip()
semrepetidas = ""
for i in palavra:
    if not i in semrepetidas:
        semrepetidas+= i

print('A palavra é:',semrepetidas)