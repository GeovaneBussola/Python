contadorchave = "sim"
contadornumero = 0
soma = 0

while contadorchave =="sim":
    contadornumero = contadornumero + 1
    numero = float(input(f'Digite o Numero {contadornumero}: '))
    soma = soma + numero
    contadorchave = input('Deseja continuar?: ')

print(f'A média desses {contadornumero} numeros é: {(soma / contadornumero)}')