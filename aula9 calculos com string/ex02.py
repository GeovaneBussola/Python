# 2- Faça um programa em Python que solicite um número inteiro de três algarismos e
# imprima a soma desse número com seu inverso. Exemplo:
# Digite um número inteiro com três algarismos: 123
# O inverso do número é: 321
# A soma é: 123 + 321 = 444

numerointeiro = input('Digite um numero inteiro com tres algarimos: ').strip()
while not (len(numerointeiro) == 3 and numerointeiro.isdigit()):
    print('Digito invalido!!')
    numerointeiro = input('Digite um numero inteiro com tres algarimos: ').strip()
numeroinverso = numerointeiro[::-1]
print('O inverso desse numero é', numeroinverso)
soma = int(numerointeiro) + int(numeroinverso)
print(f'A soma é: {numerointeiro} + {numeroinverso} = {soma}')