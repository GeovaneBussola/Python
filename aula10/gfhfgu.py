ano = int(input('Digite um ano para verificar se ele é bixesto ou não: '))
bixesto = ano % 400
if bixesto ==0:
    print(f'O ano {ano} é bixesto')
else:
    print(f'O ano {ano} não é bixesto')