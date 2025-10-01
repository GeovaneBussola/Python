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

    while True:
        try:
            espera_media.until(EC.element_to_be_clickable((By.XPATH, '//span[text()="Adicionar um usuário"]'))) # Espera adiciona novo usuario e clica
            chrome.find_element(By.XPATH, '//span[text()="Adicionar um usuário"]').click()
            break
        except TimeoutException:
            chrome.refresh()
            sleep(2)

    # Cria os registros necessarios para preencher o formulario do google adm
    for dicionario in lista_alunos: 
        nome_completo = dicionario['Nome']
        nome_dividido = nome_completo.split()
        primeiro_nome = nome_dividido[0]
        sobrenome = " ".join(nome_dividido[1:])
        gmail = f"mc.{dicionario['RM']}"
        senha = f"{dicionario['RM']}{nome_dividido[-1]}"
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

def moodle(login_moodle,senha_moodle):
    def loga_moodle():
        # Só sai do loop quando conseguir logar no moodle
        while True:
            try:
                espera.until(EC.presence_of_element_located((By.ID,'username')))
                chrome.find_element(By.ID,'username').clear()
                chrome.find_element(By.ID,'password').clear()
                chrome.find_element(By.ID,'username').send_keys(login_moodle)
                chrome.find_element(By.ID,'password').send_keys(senha_moodle)
                chrome.find_element(By.ID,'loginbtn').click()
                espera.until(EC.presence_of_element_located((By.ID,'id_username')))
                break
            except TimeoutException:
                chrome.refresh()

    def adiciona_turma(dicionario,indice=0):
            # Cria o nome do aluno com a turma para filtrar em increver usuário
            if dicionario['Turma'][2] == 'i':
                turma_para_filtro = f"Infantil {dicionario['Turma'][0]} - {dicionario['Turma'][4].upper()}"
            elif dicionario['Turma'][2] == 'f':
                turma_para_filtro = f"{dicionario['Turma'][0]} Ano {dicionario['Turma'][4].upper()}"
            elif dicionario['Turma'][2] == 'm':
                turma_para_filtro = f"{dicionario['Turma'][0]} Série {dicionario['Turma'][4].upper()}"

            # Define o link com indice caso aluno seja do ensino médio
            if dicionario['Turma'][2] != 'm':
                link_para_turma = turmas_moodle[turma]
            else:
                link_para_turma = turmas_moodle[turma][indice]

            # Clica em Inscrever usuários (Para adicionar na turma)
            chrome.get(link_para_turma)
            espera.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input.btn.btn-primary[value='Inscrever usuários']")))
            sleep(1.5)
            chrome.find_element(By.XPATH, "//input[@type='submit' and @value='Inscrever usuários']").click()

            # Escreve o filtro e adiciona na turma
            espera.until(EC.visibility_of_element_located((By.XPATH, "//input[@data-fieldtype='autocomplete']"))).send_keys(str(dicionario['RM']))
            try:
                espera.until(EC.element_to_be_clickable((By.XPATH, f"//li[.//span[text()='{dicionario['Nome']} {turma_para_filtro}']]"))).click()
            except TimeoutException:
                print(f'O aluno {dicionario['Nome']} não foi adicionado a turma')
                pass
            sleep(3)
            espera.until(EC.element_to_be_clickable((By.XPATH, "//button[text()='Inscrever usuários selecionados e coortes']"))).click()
            sleep(3.5)

    chrome.get('https://educacaocabriniana.com.br/moodle/user/editadvanced.php?id=-1') # Abre Moodle
    
    loga_moodle()

    continuar = 0 # Define variavel de ferramenta para o tratamento de erro de seção expirada

    # Cria os registros necessarios para preencher o formulario do moodle
    for dicionario in lista_alunos: 
        for i in range(2): # Esse for é um metodo para caso a sessão expire seção (logar novamente)
            rm = f"mc.{dicionario['RM']}@madrecabrini.com.br"
            nome_completo = dicionario['Nome']
            nome_dividido = nome_completo.split()
            senha = f"{dicionario['RM']}{nome_dividido[-1]}"
            if dicionario['Turma'][2] == 'i':
                turma = f"Infantil {dicionario['Turma'][0]} - {dicionario['Turma'][4].upper()}"
            elif dicionario['Turma'][2] == 'f':
                turma = f"{dicionario['Turma'][0]} Ano {dicionario['Turma'][4].upper()}"
            elif dicionario['Turma'][2] == 'm':
                turma = f"{dicionario['Turma'][0]} Série {dicionario['Turma'][4].upper()}"

            # Preenchimento dos campos do formulario
            espera.until(EC.visibility_of_element_located((By.ID, "id_username"))).send_keys(str(rm))
            
            chrome.find_element(By.XPATH, '//a[contains(., "Clique para inserir texto")]').click()

            chrome.find_element(By.ID,'id_newpassword').send_keys(senha)

            chrome.find_element(By.ID,'id_firstname').send_keys(nome_completo)

            chrome.find_element(By.ID,'id_lastname').send_keys(turma)

            chrome.find_element(By.ID,'id_email').send_keys(rm)

            # Adiciona o usuário
            criar_usuario = chrome.find_element(By.ID,'id_submitbutton')
            chrome.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", criar_usuario) # Scrola até criar usuario
            espera.until(EC.element_to_be_clickable((By.ID,'id_submitbutton')))
            criar_usuario.click()

            # Tratamento de possiveis erros (Aluno ja existe no moodle ou seção expirou)
            try:
                espera.until(EC.presence_of_element_located((By.XPATH, '//button[contains(text(), "Adicionar um novo usuário")]')))
                break
            except TimeoutException:
                try:
                    espera.until(EC.presence_of_element_located((By.ID,'username')))
                    loga_moodle()
                    continue
                except TimeoutException:
                    chrome.get('https://educacaocabriniana.com.br/moodle/user/editadvanced.php?id=-1')
                    print(f'Não foi possivel adicionar o aluno {dicionario['Nome']} no moodle')
                    continuar = 1
                    break
        if continuar == 1:
            continuar = 0
            continue
        
        # Se for o ultimo aluno da planilha ele pula a etapa de adiconar novo usuário
        if dicionario == lista_alunos[-1]:
            pass
        else:
            adicionar_um_novo_usuario = chrome.find_element(By.XPATH, '//button[contains(text(), "Adicionar um novo usuário")]')
            chrome.execute_script("arguments[0].scrollIntoView({block: 'center', behavior: 'smooth'});", adicionar_um_novo_usuario) # Scrola até adicionar um novo usuario
            espera.until(EC.element_to_be_clickable((By.XPATH, '//button[contains(text(), "Adicionar um novo usuário")]')))
            adicionar_um_novo_usuario.click()
    
    # Lista de links para os cursos no moodle
    turmas_moodle = {'1 e 2-i-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3157',
                     '1 e 2-i-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3158',
                     '3-i-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3159',
                     '3-i-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3160',
                     '3-i-c':'',
                     '4-i-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3161',
                     '4-i-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3162',
                     '4-i-c':'',
                     '5-i-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3163',
                     '5-i-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3164',
                     '5-i-c':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3165',
                     '1-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3133',
                     '1-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3137',
                     '1-f-c':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3138',
                     '1-f-d':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3139',
                     '2-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3140',
                     '2-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3141',
                     '2-f-c':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3142',
                     '3-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3144',
                     '3-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3145',
                     '3-f-c':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3146',
                     '3-f-d':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3147',
                     '4-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3148',
                     '4-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3149',
                     '4-f-c':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3150',
                     '4-f-d':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3151',
                     '4-f-e':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3152',
                     '5-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3153',
                     '5-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3154',
                     '5-f-c':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3155',
                     '5-f-d':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3156',
                     '6-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3168',
                     '6-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3167',
                     '6-f-c':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3169',
                     '6-f-d':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3170',
                     '7-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3171',
                     '7-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3172',
                     '7-f-c':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3173',
                     '8-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3174',
                     '8-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3175',
                     '9-f-a':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3176',
                     '9-f-b':'https://educacaocabriniana.com.br/moodle/user/index.php?id=3177',
                     '1-m-a':('https://educacaocabriniana.com.br/moodle/user/index.php?id=3246','https://educacaocabriniana.com.br/moodle/user/index.php?id=3248'),
                     '2-m-a':('https://educacaocabriniana.com.br/moodle/user/index.php?id=3245','https://educacaocabriniana.com.br/moodle/user/index.php?id=3249'),
                     '3-m-a':('https://educacaocabriniana.com.br/moodle/user/index.php?id=3244','https://educacaocabriniana.com.br/moodle/user/index.php?id=3250'),
                     '3-m-b':('https://educacaocabriniana.com.br/moodle/user/index.php?id=3244','https://educacaocabriniana.com.br/moodle/user/index.php?id=3251')
                     }
    
    # For para adicionar um aluno de cada vez a sua respectiva turma
    for dicionario in lista_alunos:
        # Junção das turmas dos primeiros e segundos anos do infantil
        turma = dicionario['Turma']
        if turma in ('1-i-a','2-i-a'):
            turma = '1 e 2-i-a'
        elif turma in ('1-i-b','2-i-b'):
            turma = '1 e 2-i-b'
        
        # Define quantas vezes sera necessario chamar o (adicionar_turma) com base na turma do aluno
        if dicionario['Turma'][2] != 'm':
            adiciona_turma(dicionario)
        else:
            for indice in range(len(turmas_moodle[turma])):
                adiciona_turma(dicionario,indice)
                
    chrome.get("chrome://newtab/")

def ionica(login_ionica,senha_ionica):
    chrome.get('https://madrecabrinisp.souionica.com.br/school/6d7a8ad2-16c4-11ea-8c78-bbc55ddf4924/students')

    espera.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="email"]'))).send_keys(login_ionica)
    chrome.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    sleep(20)


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

login_google = ''
senha_google = ''

login_moodle = ''
senha_moodle = ''

login_ionica = ''
senha_ionica = ''

chrome = webdriver.Chrome()
chrome.maximize_window()
espera = WebDriverWait(chrome,12)
espera_media = WebDriverWait(chrome,15)

# google(login_google,senha_google)
# moodle(login_moodle,senha_moodle)
ionica(login_ionica,senha_ionica)