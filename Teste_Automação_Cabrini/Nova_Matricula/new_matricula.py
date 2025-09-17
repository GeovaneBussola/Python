import pandas as pd
import pyautogui as auto
from time import sleep
import os

def qtd_press(tecla,vezes,tempo=0):
    for i in range(vezes):
        auto.press(tecla)
        sleep(tempo)


#Localiza e realiza a leitura da planilha
diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_planilha = os.path.join(diretorio,'planilhateste.xlsx')
planilha = pd.read_excel(r'C:\Users\geovane.bussola.MADRECABRINI\Downloads\planilhateste.xlsx')
print(planilha)

#Cria listas com Nome,RM e Datada_de_Nascimento de cada aluno na planilha
lista = []
for i in planilha.index:
    aluno = []
    lista.append(aluno)
    lista[i].append(planilha.loc[i,'Nome'])
    lista[i].append(planilha.loc[i,'RM'])
    lista[i].append(str(planilha.loc[i,'Data_de_Nascimento']))


#Inicialização do google
auto.hotkey('win','d') # Miniminiza todas janelas
auto.hotkey('ctrl','alt','c') # Abre o Chrome
sleep(5) # Espera o Chrome abrir
auto.hotkey('win','up') # Maximiza a tela caso esteja em janela


#Gmail-- Cria o gmail e a senha a partir da lista
qtd_press('tab',4) # Ir para google apps
auto.PAUSE = 0.5
auto.press('enter') # Selecionar google apps
auto.press('enter') # Abrir administrador
sleep(3)
auto.write('g61050548') # Digitar senha da conta
auto.press('enter') # Abrir conta adm
sleep(3)

for i in range(len(lista)):
    nome_completo = lista[i][0]
    nome_dividido = nome_completo.split()
    nome = nome_dividido[0]
    sobrenome = " ".join(nome_dividido[1:])
    ultimo_nome = nome_dividido[-1]
    rm = str(lista[i][1])
    gmail = f'mc.{rm}'
    senha = f'{rm}{ultimo_nome}'.lower()

    auto.PAUSE = 0
    qtd_press('tab',13) # Ir até adicionar usuario
    sleep(1)
    auto.press('enter') # Abrir adicionar usuário
    sleep(4)
    auto.write(nome)
    auto.press('tab')
    auto.write(sobrenome)
    auto.press('tab')
    auto.write(gmail)
    qtd_press('tab',4)
    auto.press('enter')
    qtd_press('tab',7)
    auto.press('right')
    auto.write(senha)
    qtd_press('tab',2)
    auto.press('space')
    sleep(10)


















