numero = 0
print('Digite 10 numeros')
for i in range(1,11):
    digitado = int(input(f"numero {i} :"))
    numero += digitado

print('A soma dos 10 numeros digitados é %d' % (numero))