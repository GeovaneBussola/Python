def linha(tam=42):
    return tam * '-'

def cabeçalho(texto):
    print(linha())
    print(texto.center(42).upper())
    print(linha())

def menu(lista):
    cabeçalho('Menuzão')
    for i in lista:
        print(f'{i[0]} - {i[1]}')
            





menu([(1,"macarrão"),(5,"feijão"),(3,"arroz")])