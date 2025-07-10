# Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaint(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError,TypeError):
            print('ERRO!')
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar o valor')
            return 0
        else:
            return num
        
def leiafloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError,TypeError):
            print('ERRO!')
        except KeyboardInterrupt:
            print('O usuario preferiu não digitar o valor')
            return 0
        else:
            return num

inteiro = leiaint('Numero inteiro: ')
real = leiafloat('Numero real: ')

print(f'O valor inteiro digitado foi {inteiro} e o valor real foi {real}')