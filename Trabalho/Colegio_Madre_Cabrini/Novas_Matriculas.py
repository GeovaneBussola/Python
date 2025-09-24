from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from pyautogui import hotkey
from pyautogui import press
from pyautogui import click
from time import sleep
import pandas as pd
import os
import pyperclip


gmail = 'a'
senha = 'a'


def logar_goole(navegador,gmail,senha,time=10):
    espera = WebDriverWait(navegador,time)

    url = navegador.current_url.lower()
    if "accounts.google.com" in url or "signin" in url:
        pass
    try:
        espera.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
        pyperclip.copy(gmail)
        hotkey('ctrl','v')
        navegador.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
    except TimeoutException:
        pass
    try:
        espera.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
        pyperclip.copy(senha)
        sleep(1)
        hotkey('ctrl','v')
        navegador.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()

    except TimeoutException:
        pass

diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_planilha = os.path.join(diretorio,'new_matricula.xlsx')
planilha = pd.read_excel(caminho_planilha)


lista_alunos = []
for linha in planilha.index:
    lista_alunos.append({
        'Nome': planilha.loc[linha,'Nome'],
        'RM': planilha.loc[linha,'RM'],
        'Data_de_Nascimento': planilha.loc[linha,'Data_de_Nascimento'],
        'Turma': planilha.loc[linha,'Turma']
    })


chrome = webdriver.Chrome()

chrome.maximize_window()

chrome.get('https://admin.google.com/?utm_source=app_launcher&pli=1&rapt=AEjHL4OWBlzd2dG79Ew2vQtTAXvlSwUj3nIC5fAaM0cW2SZnexcKkPbws4BFKBPKEvWOlWytbGD8fHZ8PyeQmZtNgiiV6xFtJsw4z390jsGjpNQuYTdg67I')

logar_goole(chrome,gmail,senha,10) # Acessa o Google Adiministrador

espera = WebDriverWait(chrome,30)

# Espera o elemento adiconar novo usuario e clica
espera.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="i7"]/ul/li[1]/div/div/button/span[5]'))) 
chrome.find_element(By.XPATH,'//*[@id="i7"]/ul/li[1]/div/div/button/span[5]').click()

for dicionario in lista_alunos:
    nome_completo = dicionario['Nome']
    nome_dividido = nome_completo.split(' ')
    primeiro_nome = nome_dividido[0]
    sobrenome = nome_dividido[1:]
    gmail = f'mc.{dicionario['RM']}'
    senha = f'{dicionario['RM']}{nome_dividido[-1]}'
    if len(senha) == 10:
        print(f'Foi incrementado um @ na senha do {nome_completo}')
        senha = f'{senha}@'

    # Espera carregar campos de preenchimento e preenche
    espera.until(EC.visibility_of_element_located((By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/input')))
    chrome.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[1]/div/div/div/div[1]/div/div[1]/input').send_keys(primeiro_nome) # Preenche o Nome
    chrome.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[1]/div[2]/div/div/div/div[1]/div/div[1]/input').send_keys(sobrenome) # Preenche o Sobrenome
    chrome.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[2]/div[1]/div[1]/div/div/div[1]/div/div[1]/input').send_keys(gmail) # Preenche o Gmail
    chrome.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[4]/div[1]/span/span/span[1]').click() # Abre gerenciar senha
    chrome.find_element(By.XPATH,'//*[@id="c164"]').click() # Seleciona Criar uma senha

    chrome.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[5]/div[4]/c-wiz/div[2]/div/div/div[1]/div/div[1]/input').send_keys(senha) # Digita a senha do novo usuario

    chrome.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[1]/span/div/div[5]/div[4]/c-wiz/div[2]/label/div/div[3]').click()

    
    adicionar_novo_usuario = chrome.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]/span/span')
    chrome.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});",adicionar_novo_usuario)
    espera.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]/span/span')))
    sleep(2)
    adicionar_novo_usuario.click()

    adicionar_outro_usuario = chrome.find_element(By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/span/div/div[4]/div[1]/div/span/span')
    espera.until(EC.element_to_be_clickable((By.XPATH,'//*[@id="yDmH0d"]/div[5]/div/div[2]/span/div/span/div/div[4]/div[1]/div/span/span')))
    if not dicionario == lista_alunos[-1]:
        adicionar_outro_usuario.click()


    sleep(5000)

