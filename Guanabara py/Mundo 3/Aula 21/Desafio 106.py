# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


c =('\033[m', # 0 Sem cor
    '\033[30;41m', # 1 Vermelho 
    '\033[30;42m', # 2 Verde
    '\033[30;43m', # 3 Amarelo
    '\033[30;44m', # 4 Azul
    '\033[30;45m', # 5 Roxo
    '\033[7;30m',  # 6 Branco
    '\033[7;40m'   # 7 Inverte
    )

def titulo(msg,cor=0):
    tamanho = len(msg) + 4
    print(c[cor],end='')
    print('~' * tamanho)
    print(f'  {msg}')
    print('~' * tamanho)
    print(c[0],end='')

def ajuda(função='',cor=0):
    print(c[cor],end='')
    help(função)
    print(c[0],end='')


while True:
    titulo('Sistema de Ajuda Pyhelp',3)
    função = str(input('Função a analisar>'))
    if função.upper() == 'FIM':
        break
    titulo(f'Analisando a função ({função})',4)
    ajuda(função,2)
titulo('Exit',1)