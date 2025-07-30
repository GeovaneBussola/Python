import pygame.display
import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice

pygame.init()

pygame.mixer.music.set_volume(0.1)

musica_de_fundo = pygame.mixer.music.load('best-game-console-301284.mp3')
pygame.mixer.music.play(-1)

barulho1 = pygame.mixer.Sound('seu-madruga-nossa.mp3')
barulho1.set_volume(0.5)
barulho2 = pygame.mixer.Sound('spring-boing.mp3')
barulho2.set_volume(0.5)
largura = 640
altura = 480

x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

x_maça = randint(0,600)
y_maça = randint(0,430)

velocidade = 5
x_controle = velocidade
y_controle = 0

pontos = 0

tamanho_cobra = 5

fonte = pygame.font.SysFont('arial',40,False,False)

relogio = pygame.time.Clock()

lista_cobra = []

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Jogooo')

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela,(0,255,0),(XeY[0],XeY[1],20,20))
    
while True:
    relogio.tick(100)
    tela.fill((255,255,255))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem,True,(0,0,0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type == KEYDOWN:
                if event.key == K_a:
                    x_controle = -velocidade    
                    y_controle = 0
                if event.key == K_d:
                    x_controle = velocidade
                    y_controle = 0
                if event.key == K_w:
                    y_controle = -velocidade
                    x_controle = 0
                if event.key == K_s:
                    y_controle = velocidade
                    x_controle = 0
    
    x_cobra += x_controle
    y_cobra += y_controle
    cobra = pygame.draw.rect(tela,(0,255,0),(x_cobra,y_cobra,20,20))
    maça = pygame.draw.rect(tela,(255,0,0),(x_maça,y_maça,20,20))
    
    if cobra.colliderect(maça):
        x_maça = randint(0,600)
        y_maça = randint(0,430) 
        pontos += 1
        tamanho_cobra+=1
        choice((barulho1,barulho2)).play()

        
    
    lista_cabeça = []
    lista_cabeça.append(x_cobra)
    lista_cabeça.append(y_cobra)
    lista_cobra.append(lista_cabeça)
    if len(lista_cobra) > tamanho_cobra:
        del lista_cobra[0]
    aumenta_cobra(lista_cobra)
    

    tela.blit(texto_formatado,(450,40))
    # pygame.draw.circle(tela,(0,0,255),(300,260),40)
    # pygame.draw.line(tela,(255,255,0),(390,0),(390,600),5)

    pygame.display.update()