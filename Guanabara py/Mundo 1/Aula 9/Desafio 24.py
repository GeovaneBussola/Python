# Exercício Python 24: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.

cidade = input('Digite sua cidade: ').strip().lower()
cidade = True if cidade.split()[0] == 'santo' else False

print(cidade)