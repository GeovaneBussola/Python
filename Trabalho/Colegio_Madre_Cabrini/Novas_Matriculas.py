from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from pyautogui import hotkey
from time import sleep
import pandas as pd
import os
import pyperclip


gmail_login_google = ''
senha_login_google = ''


def logar_goole(navegador,gmail,senha,time=10):
    espera = WebDriverWait(navegador,time)
    try:
        espera.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
        pyperclip.copy(gmail)
        hotkey('ctrl','v')
        navegador.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
    except TimeoutException:
        pass
    try:
        pyperclip.copy(senha)
        espera.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
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

logar_goole(chrome,gmail_login_google,senha_login_google,10) # Acessa o Google Adiministrador

espera = WebDriverWait(chrome,60)
while True:
    try:
        espera.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Adicionar um usuário"]'))) # Espera e adicona novo usuario e clica
        chrome.find_element(By.XPATH, '//span[text()="Adicionar um usuário"]').click()
        break
    except TimeoutException:
        chrome.refresh()
        sleep(2)

for dicionario in lista_alunos:
    nome_completo = dicionario['Nome']
    nome_dividido = nome_completo.split()
    primeiro_nome = nome_dividido[0]
    sobrenome = " ".join(nome_dividido[1:])
    gmail = f'mc.{dicionario['RM']}'
    senha = f'{dicionario['RM']}{nome_dividido[-1]}'
    if len(senha) == 10:
        print(f'Foi incrementado um @ na senha do {nome_completo}')
        senha = f'{senha}@'

    # Espera carregar campos de preenchimento e preenche
    espera.until(EC.visibility_of_element_located((By.XPATH, '//input[@aria-label="Nome *"]')))
    chrome.find_element(By.XPATH, '//input[@aria-label="Nome *"]').send_keys(primeiro_nome) # Preenche o Nome

    chrome.find_element(By.XPATH,'//input[@aria-label="Sobrenome *"]').send_keys(sobrenome) # Preenche o Sobrenome

    chrome.find_element(By.XPATH,'//input[@aria-label="E-mail principal *"]').send_keys(gmail) # Preenche o Gmail

    espera.until(EC.element_to_be_clickable((By.XPATH,'//span[text()="Gerenciar a senha, a unidade organizacional e a foto do perfil do usuário"]')))
    chrome.find_element(By.XPATH,'//span[text()="Gerenciar a senha, a unidade organizacional e a foto do perfil do usuário"]').click() # Abre gerenciar senha

    espera.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type="radio"][value="create"]')))
    chrome.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="create"]').click() # Espera e Seleciona Criar uma senha

    espera.until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Digite uma senha que tenha de 8 a 100 caracteres"]')))
    chrome.find_element(By.XPATH, '//input[@aria-label="Digite uma senha que tenha de 8 a 100 caracteres"]').send_keys(senha) # Espera e digita a senha do novo usuario

    chrome.find_element(By.XPATH, '//span[text()="Pedir para o usuário alterar a senha ao fazer login"]/preceding-sibling::div[@role="checkbox"]').click() # Desativa Pedir para o usuário alterar a senha ao fazer login
    
    adicionar_novo_usuario = chrome.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]/span/span')
    chrome.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", adicionar_novo_usuario)
    espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]/span/span')))
    
    adicionar_novo_usuario.click() # Espera e adiciona novo usuario (Finalização do preenchimento de formulario para adionar o usuario)

    if dicionario == lista_alunos[-1]: # Se for o ultimo ele nao clica em adicionar outro usuario
        pass 
    
    try:
        WebDriverWait(chrome,10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and .//span[text()="ADICIONAR OUTRO USUÁRIO"]]'))) #Espera o campo adicionar outro usuario
        chrome.find_element(By.XPATH, '//div[@role="button" and .//span[text()="ADICIONAR OUTRO USUÁRIO"]]').click() # Seleciona adicionar novo usuario

    except TimeoutException:
        print(f'Não foi possivel adicionar o usuario: {nome_completo}, (Provavelmente gmail ja existe)')
        chrome.get('https://admin.google.com/ac/users?action_id=ADD_USER&journey=1&utm_source=app_launcher')


chrome.get("chrome://newtab/")
