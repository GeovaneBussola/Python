# Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)

def leiaint(msg):
    while True:
        numero = input(msg)
        if numero.isdigit():
            numero = int(numero)
            return numero
        else:
            print('\033[31mDigite apenas um numero\033[m')

            
num = leiaint('Digite um numero: ')
print(f'Você digitou o numero {num}')