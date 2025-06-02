# Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# – IMC abaixo de 18,5: Abaixo do Peso
# – Entre 18,5 e 25: Peso Ideal
# – 25 até 30: Sobrepeso
# – 30 até 40: Obesidade
# – Acima de 40: Obesidade Mórbida

altura = float(input('Digite sua altura: '))
peso = float(input('Digite sua massa corporal: '))
imc = peso/altura**2
print('Seu imc é {:.2f}'.format(imc))
if imc < 18.5:
    print('Abaixo do Peso')
elif imc < 25:
    print('Peso ideal')
elif imc < 30.01:
    print('Sobre-peso')
elif imc < 40.01:
    print('Obesidade')
else:
    print('Obesidade mórbida')
