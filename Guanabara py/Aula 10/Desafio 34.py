salario = float(input('Digite seu salario: '))
if salario > 1250:
    print(f'O aumento foi de R${salario * 0.1:.2f} o novo salario acrecido do aumento é R${salario + (salario * 0.1):.2f}')
else:
    print(f'O aumento foi de R${salario * 0.15:.2f} o novo salario acrecido do aumento é R${salario + (salario * 0.15):2f}')
