import os
import time
def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

for i in range(6):
    print('Aamnha tem game')
    time.sleep(1)
    limpar_terminal()