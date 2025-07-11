import pygame.display
import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice

pygame.init()

pygame.mixer.music.set_volume(0.3)

musica_de_fundo = pygame.mixer.music.load('best-game-console-301284.mp3')
pygame.mixer_music.play(-1)

barulho1 = pygame.mixer.Sound('seu-madruga-nossa.mp3')
barulho1.set_volume(1)
barulho2 = pygame.mixer.Sound('spring-boing.mp3')
barulho2.set_volume(1)
largura = 640
altura = 480

x = int(largura / 2)
y = int(altura / 2)

x_azul = randint(0,600)
y_azul = randint(0,430)

pontos = 0

fonte = pygame.font.SysFont('arial',40,False,False)

relogio = pygame.time.Clock()

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Jogooo')

while True:
    relogio.tick(100)
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem,True,(255,255,255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        '''
        if event.type == KEYDOWN:
                if event.key == K_a:
                    x-=20
                if event.key == K_d:
                    x+=20
                if event.key == K_w:
                    y-=20
                if event.key == K_s:
                    y+=20
        '''
    if pygame.key.get_pressed()[K_a]:
        x-=10
    if pygame.key.get_pressed()[K_d]:
        x+=10
    if pygame.key.get_pressed()[K_w]:
        y-=10
    if pygame.key.get_pressed()[K_s]:
        y+=10

    ret_vermelho = pygame.draw.rect(tela,(255,0,0),(x,y,40,50))
    ret_azul = pygame.draw.rect(tela,(0,0,255),(x_azul,y_azul,40,50))
    
    if ret_vermelho.colliderect(ret_azul):
        x_azul = randint(0,600)
        y_azul = randint(0,430) 
        pontos += 1
        choice([barulho1,barulho2]).play()
        
        
    tela.blit(texto_formatado,(450,40))
    # pygame.draw.circle(tela,(0,0,255),(300,260),40)
    # pygame.draw.line(tela,(255,255,0),(390,0),(390,600),5)

    pygame.display.update()