# def soma(num):
#     print(f'O resultado da soma é {num + 1}')
# n=int(input('Digite um valor para somar com outro: '))
# soma(n)


# def teste(a1,a2):
#     print(a1)
#     print(a2)
# a="amanha"
# b="hoje"
# teste(a,b)


def dobra(lst):
    for i in lst:
        a = i * 2
        lista_dobrada.append(a)
    print(lista_dobrada)


lista=[1,6,3,7,20,0]
lista_dobrada=[]
dobra(lista)
