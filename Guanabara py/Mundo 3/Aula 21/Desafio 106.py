# Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, o programa se encerrará. Importante: use cores.


while True:
    print(f'\033[30;46m{27*"~"}')
    print(f'{"Sistema de ajuda PyHelp":^27}')
    print(f'{27*"~"}\033[m')
    b = input('Função da bliblioteca> ')
    if b.upper() == 'STOP':
       break
    linha = f'Comando "{b}"'
    print(f"\033[43m{'~' * (len(linha) + 4)}")
    print(f'{linha:^{len(linha) + 4}}')
    print(f"{'~' * (len(linha) + 4)}\033[45m")
    help(b)
    
print(f'\033[41mExit')
    
