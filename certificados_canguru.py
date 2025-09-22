import pyautogui as auto
from time import sleep
from pyperclip import paste
import shutil
import os
#Para este programa funcinar o moodle deve estar aberto na parte de adicionar o arquivo para o aluno do lado esquerdo da tela, e o gerenciador de arquivos do lado direito. moodle 67%


posicao_img = (766,125,125,17)
auto.PAUSE = 0.3
pasta = r'C:\Users\geovane.bussola.MADRECABRINI\Downloads\Preciso_postar\Certificados 2025'

auto.hotkey('win','down')

quantidade_arquivos_na_pasta = 2

while quantidade_arquivos_na_pasta > 1:
    quantidade_arquivos_na_pasta = len([f for f in os.listdir(pasta) if os.path.isfile(os.path.join(pasta, f))])

    auto.click(x=1192, y=242)
    auto.press('f2')
    auto.hotkey('ctrl','c')
    sleep(0.5)

    nome_do_arquivo = paste().strip()

    destino_encontrou = rf'C:\Users\geovane.bussola.MADRECABRINI\Downloads\Preciso_postar\jaEnviados\{nome_do_arquivo}.pdf'
    destino_naoencontrou = rf'C:\Users\geovane.bussola.MADRECABRINI\Downloads\Preciso_postar\naoEnviados\{nome_do_arquivo}.pdf'

    #Local atual do aquivo
    origem = rf'{pasta}\{nome_do_arquivo}.pdf'

    auto.click(x=839, y=100)
    auto.hotkey('ctrl','v')
    sleep(2)

    try:
        recebe = auto.locateOnScreen("nenhum_usuario.png",posicao_img)
        if os.path.exists(origem):
            shutil.move(origem,destino_naoencontrou)
        auto.hotkey('ctrl','a')
        auto.press('backspace')
        sleep(1)
    except:
        auto.click(x=847, y=142)
        auto.moveTo(x=1222, y=244)
        auto.mouseDown()
        auto.moveTo(x=801, y=900, duration=1)
        sleep(4)
        auto.mouseUp()
        sleep(15)
        auto.click(x=329, y=1022)
        sleep(7)
        if os.path.exists(origem):
            shutil.move(origem,destino_encontrou)
        sleep(3.5)
    