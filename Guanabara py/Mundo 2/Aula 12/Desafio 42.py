# Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# – EQUILÁTERO: todos os lados iguais
# – ISÓSCELES: dois lados iguais, um diferente
# – ESCALENO: todos os lados diferentes

a = float(input('Digite o valor do primeiro lado: '))
b = float(input('Digite o valor do segundo lado: '))
c = float(input('Digite o valor do terceiro lado: '))

if a + b > c and b + c > a and a + c > b:
    if a == b == c:
        print('Pode formar um tiangulo Equilátero')
    elif a == b or a == c or b == c:
        print('Pode formar um triangulo Isósceles')
    else:
        print('Pode formar um triangulo Escaleno')
else:
    print('Nao pode formar um trigandulo')