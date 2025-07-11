def leiaint(msg=''):
    while True:
        try:
            return int(input(msg))
        except:
            print('\033[31mDigite um numero inteiro valido\033[m')

def linha(tam=42):
    return tam * '-'

def cabeçalho(texto):
    print(linha())
    print(texto.center(42).upper())
    print(linha())

def menu(lista):
    cabeçalho('Menuzão')
    for i in lista:
        print(f'\033[33m{i[0]}\033[m - \033[34m{i[1]}\033[m')
    print(linha())
    return leiaint('\033[33mOpção:\033[m')
