#Faça um programa em Python que solicite ao usuário sua altura e sexo, calcule e
#imprima o seu peso ideal. Utilize a seguinte convenção:
#▪ Para homens: (72.7*h) – 58
#▪ Para mulheres: (62.1*h) – 44.7

sexo = input('Digite seu sexo: ').lower().strip()
altura = float(input('Digite sua altura: '))
if sexo == "masculino" or sexo == "m":
    print(f'Seu peso ideal seria: {(72.7*altura) - 58:.2f}')
elif sexo == "feminino" or sexo == "f":
    print(f'Seu peso ideal seria: {(62.1*altura) - 44.7:.2f}')
else:
    print("Sexo invalido")

