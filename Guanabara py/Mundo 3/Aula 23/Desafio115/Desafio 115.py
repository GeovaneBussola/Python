from pacote.interface import *
from pacote.arquivo import *
from time import sleep

arquivo = 'geovane.txt'

if arquivoexiste(arquivo) == False:
    criararquivo(arquivo)   

while True:
    opção = menu([(1,"Ver pessoas cadastradas"),(2,"Cadastrar pessoas"),(3,"Sair")])
    if opção == 1:
        lerarquivo(arquivo)
    elif opção == 2:
        cabeçalho('Novo cadastro')
        nome = str(input('Nome:'))
        idade = leiaint('Idade:')
        cadastrar(arquivo,nome,idade)
    elif opção == 3:
        cabeçalho('Saindo do sistema, até logo...')
        break
    else:
        print('\033[31mOPÇÃO INVALIDA\033[m')
    sleep(1)
