from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from pyautogui import hotkey

from time import sleep
import pandas as pd
import os
import pyperclip



def logar_goole(navegador,time=10):
    espera = WebDriverWait(navegador,time)

    url = navegador.current_url.lower()
    if "accounts.google.com" in url or "signin" in url:
        pass
    try:
        espera.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
        gmail = "geovane.bussola@madrecabrini.com.br"
        pyperclip.copy(gmail)
        hotkey('ctrl','v')
        navegador.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
    except TimeoutException:
        pass
    try:
        espera.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
        senha = 'g61050548'
        pyperclip.copy(senha)
        sleep(1)
        hotkey('ctrl','v')
        navegador.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()
        sleep(30)

    except TimeoutException:
        pass

diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_planilha = os.path.join(diretorio,'new_matricula.xlsx')
planilha = pd.read_excel(caminho_planilha)


lista_alunos = []
for linha in planilha.index:
    lista_alunos.append({
        'nome': planilha.loc[linha,'Nome'],
        'RM': planilha.loc[linha,'RM'],
        'Data_de_Nascimento': planilha.loc[linha,'Data_de_Nascimento'],
        'Turma': planilha.loc[linha,'Turma']
    })


chrome = webdriver.Chrome()

chrome.maximize_window()

chrome.get('https://admin.google.com/?utm_source=app_launcher&pli=1&rapt=AEjHL4OWBlzd2dG79Ew2vQtTAXvlSwUj3nIC5fAaM0cW2SZnexcKkPbws4BFKBPKEvWOlWytbGD8fHZ8PyeQmZtNgiiV6xFtJsw4z390jsGjpNQuYTdg67I')

if logar_goole(chrome,10):
    print('pediu login')
    sleep(20)

else:
    print('nao pediu login')
print('deu certo')

sleep(4)