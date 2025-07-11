categorias = ["a","b","c"]
categoria = input('Digite sua categoria: ').lower()
while categoria not in categorias:
    categoria = input('Categoria invalida, porfavor digite uma categoria existente: ')

if categoria == "a":
    print('Seu salário é: R$1500,00')
elif categoria == "b":
    print('Seu salário é: R$2000,00')
elif categoria == "c":
    print('Seu salário é: R$2500,00')

