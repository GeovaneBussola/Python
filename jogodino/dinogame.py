import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
from random import choice

pygame.init()
pygame.mixer.init()

aleatorio = choice([0,1])

pontos = 0
velocidade_jogo = 10

def exibe_mensagem(msg,tamanho,cor):
    fonte = pygame.font.SysFont('comicsansms',tamanho,True,False)
    mensagem = f'{msg}'
    texto_formatado = fonte.render(mensagem,True,cor)
    return texto_formatado

def reiniciar_jogo():
    global pontos,velocidade_jogo,colidiu,aleatorio
    pontos = 0
    velocidade_jogo = 10
    colidiu = False
    dino.rect.y = altura - 64 -96 // 2
    dino.pulo = False
    dinovoador.rect.x = largura
    cacto.rect.x = largura
    aleatorio = choice([0,1])

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, 'imagens')
diretorio_sons = os.path.join(diretorio_principal,'sons')

largura = 640
altura = 480

branco = (255,255,255)
preto = (0,0,0)

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Dino')

sprite_sheat = pygame.image.load(os.path.join(diretorio_imagens,'dinoSpritesheet.png')).convert_alpha()

som_colisao = pygame.mixer.Sound(os.path.join(diretorio_sons,'death_sound.wav'))
som_colisao.set_volume(1)

som_pontuaçao = pygame.mixer.Sound(os.path.join(diretorio_sons,'score_sound.wav'))
som_pontuaçao.set_volume(1)

colidiu = False

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.som_pulo = pygame.mixer.Sound(os.path.join(diretorio_sons,'jump_sound.wav'))
        self.som_pulo.set_volume(1)
        self.imagens_dinossauro = []
        for i in range(3):
            img = self.img1 = sprite_sheat.subsurface((i * 32,0),(32,32))
            img = pygame.transform.scale(img,(32*3, 32*3))
            self.imagens_dinossauro.append(img)
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.pos_y_inicial = altura - 64 -96 //2
        self.rect.center = (100,altura - 64)
        self.pulo = False
    def pular(self):
        self.pulo = True
        self.som_pulo.play()
    def update(self):
        if self.pulo:
            self.rect.y-= 20
            if self.rect.y <= 200:
                self.pulo = False
        else:
            if self.rect.y < self.pos_y_inicial:
                self.rect.y += 15
            else:
                self.rect.y = self.pos_y_inicial
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_dinossauro[int(self.index_lista)]


class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheat.subsurface((7*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(3*32,32*3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50,200,50)
        self.rect.x = largura - randrange(30,300,90)
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
            self.rect.y = randrange(0,150,50)
        self.rect.x -= 5


class Chao(pygame.sprite.Sprite):
    def __init__(self,pos_x):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheat.subsurface((6*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(2*32,32*2))
        self.rect = self.image.get_rect()
        self.rect.y = altura - 64
        self.rect.x = pos_x * 64
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= velocidade_jogo


class Cacto(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheat.subsurface((5*32,0),(32,32))
        self.image = pygame.transform.scale(self.image,(2*32,32*2))
        self.rect = self.image.get_rect()
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (largura,altura - 64)
        self.rect.x = largura
        self.aleatorio = aleatorio
    def update(self):
        if self.aleatorio == 0:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo

class DinoVoador(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for i in range(3,5):
            img = sprite_sheat.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(32*3,32*3))
            self.imagens_dinossauro.append(img)
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.mask = pygame.mask.from_surface(self.image)
        self.rect = self.image.get_rect()
        self.rect.center = (largura,300)
        self.rect.x = largura
        self.aleatorio = aleatorio
    def update(self):
        if self.aleatorio == 1:
            if self.rect.topright[0] < 0:
                self.rect.x = largura
            self.rect.x -= velocidade_jogo
            if self.index_lista > 1:
                self.index_lista = 0
            self.index_lista += 0.25
            self.image = self.imagens_dinossauro[int(self.index_lista)]

todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)
for i in range(4):
    nuven = Nuvens()
    todas_as_sprites.add(nuven)
for i in range(20):
    chao = Chao(i)
    todas_as_sprites.add(chao)
cacto = Cacto()
todas_as_sprites.add(cacto)
dinovoador = DinoVoador()
todas_as_sprites.add(dinovoador)


relogio = pygame.time.Clock()
grupo_obstaculos = pygame.sprite.Group()
grupo_obstaculos.add(cacto)
grupo_obstaculos.add(dinovoador)
while True:
    relogio.tick(30)
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:   
            if event.key == K_SPACE or K_w:
                if dino.rect.y != dino.pos_y_inicial:
                    pass
                else:
                    if not colidiu:
                        dino.pular()

            if event.key == K_r and colidiu == True:
                reiniciar_jogo()

    colisoes = pygame.sprite.spritecollide(dino,grupo_obstaculos,False,pygame.sprite.collide_mask)
    
    todas_as_sprites.draw(tela)

    if cacto.rect.topright[0] < 0 or dinovoador.rect.topright[0] < 0:
        escolha_obstaculo = choice([0,1])
        cacto.rect.x = largura
        dinovoador.rect.x = largura
        cacto.aleatorio = escolha_obstaculo
        dinovoador.aleatorio = escolha_obstaculo

    if colisoes and colidiu == False:
        som_colisao.play()
        colidiu = True
    if colidiu:
        if pontos % 100 == 0:
            pontos+=1
        gameover = exibe_mensagem('GAME OVER',40,(0,0,0))
        tela.blit(gameover,(largura//2,altura//2))
        pressr = exibe_mensagem('Pressione \'r\' para reiniciar',20,(0,0,0))
        tela.blit(pressr,(largura//2,altura//2 + 60))

    else:
        pontos+=1
        todas_as_sprites.update()
        mensagem = exibe_mensagem(pontos,40,(0,0,0))
    if pontos % 100 == 0:
        som_pontuaçao.play()
        if velocidade_jogo >= 23:
            velocidade_jogo+=0
        else:
            velocidade_jogo+=1
    
    tela.blit(mensagem,(520,30))
    pygame.display.flip()


