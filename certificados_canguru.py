import pyautogui as auto
from time import sleep
from pyperclip import paste
import shutil
import os
#Para este programa funcinar o moodle deve estar aberto na parte de adicionar o arquivo para o aluno do lado esquerdo da tela, e o gerenciador de arquivos do lado direito.


posicao_img = (766,125,125,17)

pasta = r'C:\Users\geovane.bussola.MADRECABRINI\Downloads\Preciso_postar\Certificados 2025'

destino_encontrou = rf'C:\Users\geovane.bussola.MADRECABRINI\Downloads\Preciso_postar\jaEnviados\{paste()}.pdf'
destino_naoencontrou = rf'C:\Users\geovane.bussola.MADRECABRINI\Downloads\Preciso_postar\naoEnviados\{paste()}.pdf'


quantidade_arquivos_na_pasta = len([f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))])
auto.click(x=1192, y=242)
auto.press('f2')
auto.hotkey('ctrl','c')

#Local atual do aquivo
origem = rf'{pasta}\{paste()}.pdf'

auto.click(x=839, y=107)
auto.hotkey('ctrl','v')
sleep(2.5)

try:
    recebe = auto.locateOnScreen("nenhum_usuario.png",posicao_img)
    shutil.move(origem,destino_naoencontrou)
    auto.hotkey('ctrl','a')
    auto.press('backspace')
    sleep(1)
    

except:
    shutil.move(origem,destino_encontrou)
    

    
    