from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from pyautogui import hotkey
from time import sleep
import pandas as pd
import os
import pyperclip


def google(login_google,senha_google):
    chrome.get('https://admin.google.com/?utm_source=app_launcher&pli=1&rapt=AEjHL4OWBlzd2dG79Ew2vQtTAXvlSwUj3nIC5fAaM0cW2SZnexcKkPbws4BFKBPKEvWOlWytbGD8fHZ8PyeQmZtNgiiV6xFtJsw4z390jsGjpNQuYTdg67I')

    try:
        espera.until(EC.presence_of_element_located((By.XPATH,'//*[@id="identifierId"]')))
        pyperclip.copy(login_google)
        hotkey('ctrl','v')
        chrome.find_element(By.XPATH,'//*[@id="identifierNext"]/div/button/span').click()
    except TimeoutException:
        pass

    try:
        pyperclip.copy(senha_google)
        espera.until(EC.presence_of_element_located((By.XPATH,'//*[@id="password"]/div[1]/div/div[1]/input')))
        sleep(1)
        hotkey('ctrl','v')
        chrome.find_element(By.XPATH,'//*[@id="passwordNext"]/div/button/span').click()
    except TimeoutException:
        pass

    espera = WebDriverWait(chrome,60)
    while True:
        try:
            espera.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Adicionar um usuário"]'))) # Espera e adicona novo usuario e clica
            chrome.find_element(By.XPATH, '//span[text()="Adicionar um usuário"]').click()
            break
        except TimeoutException:
            chrome.refresh()
            sleep(2)

    for dicionario in lista_alunos: # Cria os registros necessarios para preencher o formulario do google adm
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
        chrome.find_element(By.CSS_SELECTOR, 'input[type="radio"][value="create"]').click() # Criar uma senha

        espera.until(EC.presence_of_element_located((By.XPATH, '//input[@aria-label="Digite uma senha que tenha de 8 a 100 caracteres"]')))
        chrome.find_element(By.XPATH, '//input[@aria-label="Digite uma senha que tenha de 8 a 100 caracteres"]').send_keys(senha) # Digita a senha do novo usuario

        chrome.find_element(By.XPATH, '//span[text()="Pedir para o usuário alterar a senha ao fazer login"]/preceding-sibling::div[@role="checkbox"]').click() # Desativa Pedir para o usuário alterar a senha ao fazer login
        
        adicionar_novo_usuario = chrome.find_element(By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]/span/span')
        chrome.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", adicionar_novo_usuario) # Scrola até adicionar novo usuario
        espera.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="yDmH0d"]/div[5]/div/div[2]/span/c-wiz/div/span/div/c-wiz/div[2]/div[2]/span/span')))
        
        adicionar_novo_usuario.click() # Adiciona novo usuario (Finalização do preenchimento de formulario para adionar o usuario)

        try:
            WebDriverWait(chrome,10).until(EC.element_to_be_clickable((By.XPATH, '//div[@role="button" and .//span[text()="ADICIONAR OUTRO USUÁRIO"]]'))) #Espera o campo adicionar outro usuario
            
        except TimeoutException:
            print(f'Não foi possivel adicionar o usuario: {nome_completo}, (Provavelmente gmail ja existe)')
            chrome.get('https://admin.google.com/ac/users?action_id=ADD_USER&journey=1&utm_source=app_launcher')
            continue

        if dicionario == lista_alunos[-1]: # Se for o ultimo ele nao clica em adicionar outro usuario
            pass
        else:
            chrome.find_element(By.XPATH, '//div[@role="button" and .//span[text()="ADICIONAR OUTRO USUÁRIO"]]').click() # Seleciona adicionar novo usuario

    chrome.get("chrome://newtab/")


# Acessa a planilha
diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_planilha = os.path.join(diretorio,'new_matricula.xlsx')
planilha = pd.read_excel(caminho_planilha)

# Cria dicionario com informações do aluno e guarda em uma lista
lista_alunos = []
for linha in planilha.index:
    lista_alunos.append({
        'Nome': planilha.loc[linha,'Nome'],
        'RM': planilha.loc[linha,'RM'],
        'Data_de_Nascimento': planilha.loc[linha,'Data_de_Nascimento'],
        'Turma': planilha.loc[linha,'Turma']
    })


login_moodle = ''
senha_moodle = ''

# options = Options()
# options.page_load_strategy = 'none'
# service=Service(), options=options

chrome = webdriver.Chrome()
chrome.maximize_window()
espera = WebDriverWait(chrome,20)


def moodle(login_moodle,senha_moodle):
    chrome.get('https://educacaocabriniana.com.br/moodle/user/editadvanced.php?id=-1') # Abre Moodle
    # Loga no moodle
    while True:
        try:
            espera.until(EC.presence_of_element_located((By.ID,'username')))
            chrome.find_element(By.ID,'username').send_keys(login_moodle)
            chrome.find_element(By.ID,'password').send_keys(senha_moodle)
            chrome.find_element(By.ID,'loginbtn').click()
            espera.until(EC.presence_of_element_located((By.ID,'id_username')))
            break
        except TimeoutException:
            chrome.refresh()
            espera.until(EC.presence_of_element_located((By.ID,'username')))
            chrome.find_element(By.ID,'username').clear()
            chrome.find_element(By.ID,'password').clear()

    for dicionario in lista_alunos: # Cria os registros necessarios para preencher o formulario do moodle
        rm = f'mc.{dicionario['RM']}@madrecabrini.com.br'
        nome_completo = dicionario['Nome']
        nome_dividido = nome_completo.split()
        senha = f'{dicionario['RM']}{nome_dividido[-1]}'
        if dicionario['Turma'][2] == 'i':
            turma = f'Infantil {dicionario['Turma'][0]} - {dicionario['Turma'][4].upper()}'
        elif dicionario['Turma'][2] == 'f':
            turma = f'{dicionario['Turma'][0]} Ano {dicionario['Turma'][4].upper()}'
        elif dicionario['Turma'][2] == 'm':
            turma = f'{dicionario['Turma'][0]} Série {dicionario['Turma'][4].upper()}'

        espera.until(EC.presence_of_element_located((By.ID,'id_username')))
        chrome.find_element(By.ID,'id_username').send_keys(rm)

        chrome.find_element(By.XPATH, '//a[contains(., "Clique para inserir texto")]').click()

        chrome.find_element(By.ID,'id_newpassword').send_keys(senha)

        chrome.find_element(By.ID,'id_firstname').send_keys(nome_completo)

        chrome.find_element(By.ID,'id_lastname').send_keys(turma)

        chrome.find_element(By.ID,'id_email').send_keys(rm)

        criar_usuario = chrome.find_element(By.ID,'id_submitbutton')
        chrome.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", criar_usuario) # Scrola até criar usuario
        espera.until(EC.element_to_be_clickable((By.ID,'id_submitbutton')))
        criar_usuario.click()
        try:
            espera.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Adicionar um novo usuário")]')))
        except TimeoutException:
            print(f'Não foi possivel adicionar o usuario {nome_completo} no moodle (Provavelmente gmail ja existe)')
            chrome.get('https://educacaocabriniana.com.br/moodle/user/editadvanced.php?id=-1')
            continue
            
        if dicionario == lista_alunos[-1]:
            pass
        else:
            adicionar_um_novo_usuario = chrome.find_element(By.XPATH, '//button[contains(text(), "Adicionar um novo usuário")]')
            chrome.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", adicionar_um_novo_usuario) # Scrola até adicionar um novo usuario
            espera.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Adicionar um novo usuário")]')))
            adicionar_um_novo_usuario.click()


moodle(login_moodle,senha_moodle)