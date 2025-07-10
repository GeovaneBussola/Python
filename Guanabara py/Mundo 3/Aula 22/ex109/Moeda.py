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

