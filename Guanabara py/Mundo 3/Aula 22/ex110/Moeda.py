def moeda(numero):
    return f'R${numero:.2f}'.replace('.',',')

def dobra(numero,formatar=False):
    numero*=2
    if formatar:
        numero=moeda(numero)
    return numero

def metade(numero,formatar=False):
    numero/=2
    if formatar:
        numero=moeda(numero)
    return numero

def aumenta(numero,taxa,formatar=False):
    numero = numero + (numero*taxa/100)
    if formatar:
        numero=moeda(numero)
    return numero

def reduz(numero,taxa,formatar=False):
    numero = numero - (numero*taxa/100)
    if formatar:
        numero=moeda(numero)
    return numero

def resumo(numero,taxa=0,taxar=0):
    print(30*'-')
    print(f'{"RESUMO DO VALOR":^30}')
    print(30*'-')
    print(f'Preço analisado: {moeda(numero)}')
    print(35*'-')
    print(f'Dobro do preço:\t\t{dobra(numero,True)}')
    print(f'Metade do preço:\t{metade(numero,True)}')
    print(f'{taxa}% de aumento:\t\t{aumenta(numero,taxa,True)}')
    print(f'{taxar}% de redução:\t\t{reduz(numero,taxar,True)}')
    print(35*'-')