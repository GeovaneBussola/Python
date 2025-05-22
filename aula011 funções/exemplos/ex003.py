# Escreva um método chamado calculaIMC que receba o peso e altura de uma pessoa,
# calcule e retorne o IMC, de acordo com a fórmula abaixo:
# imc = peso / altura²
# Faça um programa principal que solicite ao usuário seu peso (em kg) e sua altura (em
# m) e, usando o método definido acima, mostre o IMC.

def calcula_imc(peso,altura):
    imc = peso / altura**2
    return imc
peso=float(input('Digite seu peso: '))
altura=float(input('Digite sua altura: '))
imc=calcula_imc(peso,altura)
print(f'seu imc é: {imc}')