def leiadinheiro(msg):
    while True:
        dinheiro = input(msg).replace(',','.').strip()
        if dinheiro.isalpha() or dinheiro =='':
            print('\033[31mErro, digite um numero valido\033[m')
        else:
            return float(dinheiro)