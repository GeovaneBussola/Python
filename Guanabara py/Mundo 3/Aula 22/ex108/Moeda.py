def dobra(numero):
    numero*=2
    return numero

def metade(numero):
    numero/=2
    return numero

def aumenta(numero,taxa):
    numero = numero + (numero*taxa/100)
    return numero

def reduz(numero,taxa):
    numero = numero - (numero*taxa/100)
    return numero

def moeda(numero):
    return f'R${numero:.2f}'.replace('.',',')