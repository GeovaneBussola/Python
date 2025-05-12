# 3- Elabore um programa em Python que leia uma string, converta para caixa alta e
# imprima quantas vezes cada caractere aparece nessa string. Exemplo:
# Entrada:
# • Entre com uma string: TTAAC
# Saída:
# • O caractere T aparece 2 vezes
# • O caractere A aparece 2 vezes
# • O caractere C aparece 1 vez

string = input('Digite uma string: ').upper().strip().replace(" ", "")
resultado=""
for i in string:
    if i not in resultado:
        qnt = string.count(i)
        print(f'O caractere {i} aparece {qnt} vezes')
        resultado+=i