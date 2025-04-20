#Elabore um programa em Python que implemente uma
#calculadora com as funções de somar, subtrair, multiplicar e
#dividir. O programa deverá solicitar ao usuário os dois
#valores, e perguntar qual a operação pretendida (‘+’, ‘-‘ , ‘*’ ou
#‘/’ ) e a seguir calcular e mostrar o resultado.
vl1 = float(input("Digite um valor: "))
vl2 = float(input('Digite o segundo valor: '))
sinal = input('Digite o sinal para fazer o calculo: ')
if sinal=="+":
    conta = vl1 + vl2
    print(f"A soma de {vl1:.2f} com {vl2:.2f} é: {conta:.2f}")
elif sinal=="-":
    conta = vl1 - vl2
    print(f"A subtração de {vl1:.2f} com {vl2:.2f} é: {conta:.2f}")
elif sinal=="*":
    conta = vl1 * vl2
    print(f"A multiplicação de {vl1:.2f} com {vl2:.2f} é: {conta:.2f}")
elif sinal=="/":
    conta = vl1 / vl2
    print(f"A divisão de {vl1:.2f} com {vl2:.0f} é: {conta:.2f}")
else:
    print("Sinal invalido")