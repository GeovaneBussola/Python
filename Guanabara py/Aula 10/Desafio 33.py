n1 = float(input('Digite o primeiro numero: '))
n2 = float(input('Digite o segundo numero: '))
n3 = float(input('Digite o terceiro numero: '))

if n1 >= n2 and n1 >= n3:
    print(n1)
elif n2>= n3:
    print(n2)
else:
    print(n3)