# Exercício Python 26: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

frase = str(input('Digite um texto: ')).strip()

print(f'O A aparece {frase.lower().count("a")} vezes na frase')

print(f'A primeira vez que o A aparece é na posção {frase.find("a")+1} e ultima vez é {frase.rfind("a")+1}')