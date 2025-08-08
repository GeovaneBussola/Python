import pygame
from pygame.locals import *
from sys import exit
import os
from random import choice
pygame.init()

largura = 1080
altura = 720

velocidade = 10
velocidade_pulo = 22
tamanho_mago = 3

vivo = True

tela = pygame.display.set_mode((largura,altura))

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal,'sprites')

ataque = pygame.image.load(os.path.join(diretorio_imagens,'ataque.png'))
correrdireita = pygame.image.load(os.path.join(diretorio_imagens,'correrdireita.png'))
correresquerda = pygame.image.load(os.path.join(diretorio_imagens,'correresquerda.png'))
morrer = pygame.image.load(os.path.join(diretorio_imagens,'morrer.png'))
parado = pygame.image.load(os.path.join(diretorio_imagens,'parado.png'))
paradoesquerda = pygame.image.load(os.path.join(diretorio_imagens,'paradoesquerda.png'))
pulodireita = pygame.image.load(os.path.join(diretorio_imagens,'pulodireita.png'))
puloesquerda = pygame.image.load(os.path.join(diretorio_imagens,'puloesquerda.png'))
inimigo = pygame.image.load(os.path.join(diretorio_imagens,'inimigo.png'))
bola_de_fogo_direita = pygame.image.load(os.path.join(diretorio_imagens,'bola_de_fogo_direita.png'))
bola_de_fogo_esquerda = pygame.image.load(os.path.join(diretorio_imagens,'bola_de_fogo_esquerda.png'))

fundo = pygame.image.load(os.path.join(diretorio_imagens,'floresta.png'))
tela_de_fundo = pygame.transform.scale(fundo,(largura,altura))

pygame.display.set_caption('Mago')

relogio = pygame.time.Clock()

class Mago(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pulos = 0
        self.velocidade_y = 0
        self.gravidade = 1.7
        self.pulo_força = -22
        self.no_chao = True
        self.virado_para_direita = True
        self.direita = False
        self.esquerda = False
        self.altura_inicial = altura - 200
        self.spritesparado = []
        for i in range(9):
            img = parado.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(tamanho_mago*32,tamanho_mago*32))
            self.spritesparado.append(img)
        self.spriteparadoesquerda = []
        for i in range(9):
            img = paradoesquerda.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(tamanho_mago*32,tamanho_mago*32))
            self.spriteparadoesquerda.append(img)
        self.correrdireita = []
        for i in range(8):
            img = correrdireita.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(tamanho_mago*32,tamanho_mago*32))
            self.correrdireita.append(img)
        self.correresquerda = []
        for i in range(8):
            img = correresquerda.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(tamanho_mago*32,tamanho_mago*32))
            self.correresquerda.append(img)
        self.pulodireita_subindo = []
        for i in range(7):
            img = pulodireita.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(tamanho_mago*3,tamanho_mago*3))
            self.pulodireita_subindo.append(img)
        self.index_sprite = 0
        self.image = self.spritesparado[self.index_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = self.altura_inicial
    def update(self):
        self.velocidade_y += self.gravidade
        self.rect.y += self.velocidade_y
        if self.rect.y >= self.altura_inicial:
            self.rect.y = self.altura_inicial
            self.velocidade_y = 0
            self.no_chao = True
            self.pulos = 0
        if self.direita:
            if self.index_sprite > 7:
                self.index_sprite = 0
            if self.rect.x < largura - 60:
                self.rect.x += velocidade
            self.image = self.correrdireita[int(self.index_sprite)]
            self.index_sprite += 0.3
        elif self.esquerda:
            if self.index_sprite > 7:
                self.index_sprite = 0
            if self.rect.x > -30:
                self.rect.x -= velocidade
            self.image = self.correresquerda[int(self.index_sprite)]
            self.index_sprite += 0.3
        else:
            if self.virado_para_direita:
                if self.index_sprite > 8:
                    self.index_sprite = 0
                self.image = self.spritesparado[int(self.index_sprite)]
                self.index_sprite+=0.15
            else:
                if self.index_sprite > 8:
                    self.index_sprite = 0
                self.image = self.spriteparadoesquerda[int(self.index_sprite)]
                self.index_sprite += 0.15          

class Inimigo(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.vida = 100
        self.inimigolist = []
        for i in range(9):
            img = inimigo.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(tamanho_mago*32,tamanho_mago*32))
            self.inimigolist.append(img)
        self.index = 0
        self.image = self.inimigolist[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = 800
        self.rect.y = altura - 200
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        if self.index > 8:
            self.index = 0
        self.image = self.inimigolist[int(self.index)]
        self.index += 0.2
    
class Firebol(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.firebol_list = []
        for i in range(6):
            img = bola_de_fogo_direita.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(3*32,3*32))
            self.firebol_list.append(img)
        self.index = 0
        self.image = self.firebol_list[self.index]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        if self.index > 5:
            self.index = 0
        if self.rect.x < largura:
            self.rect.x += 20
        else:
            self.kill()
        self.image = self.firebol_list[int(self.index)]
        self.index += 0.2

class Firebolesquerda(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.firebol_list_esquerda = []
        for i in range(6):
            img = bola_de_fogo_esquerda.subsurface((i*32,0),(32,32))
            img = pygame.transform.scale(img,(3*32,3*32))
            self.firebol_list_esquerda.append(img)
        self.index = 0
        self.image = self.firebol_list_esquerda[self.index]
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x
        self.rect.y = y
        self.mask = pygame.mask.from_surface(self.image)
    def update(self):
        if self.index > 5:
            self.index = 0
        if self.rect.x < largura:
            self.rect.x -= 20
        else:
            self.kill()
        self.image = self.firebol_list_esquerda[int(self.index)]
        self.index += 0.2

todas_sprites = pygame.sprite.Group()
bolas_de_fogo = pygame.sprite.Group()
inimigos = pygame.sprite.Group()
mago = Mago()
inimigo = Inimigo()

todas_sprites.add(mago)
todas_sprites.add(inimigo)
inimigos.add(inimigo)

while True:
    relogio.tick(30)
    tela.blit(tela_de_fundo,(0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if (event.key == K_w or event.key == K_SPACE) and mago.pulos < 2:
                if mago.pulos == 0:
                    mago.velocidade_y = mago.pulo_força
                else:
                    mago.velocidade_y = 0
                    mago.velocidade_y += mago.pulo_força * 0.8
                mago.pulos += 1
            if event.key == K_e:
                if mago.esquerda or mago.virado_para_direita == False:
                    firebolesquerda = Firebolesquerda(mago.rect.centerx - 80, mago.rect.centery - 45)
                    bolas_de_fogo.add(firebolesquerda)
                    todas_sprites.add(firebolesquerda)
                else:
                    firebol = Firebol(mago.rect.centerx - 15, mago.rect.centery - 45)
                    bolas_de_fogo.add(firebol)
                    todas_sprites.add(firebol)

    colisoes_bola_inimigo = pygame.sprite.groupcollide(bolas_de_fogo, inimigos, True, False, pygame.sprite.collide_mask)
    if colisoes_bola_inimigo:
        inimigo.vida -= 20
    if inimigo.vida <=0:
        inimigo.kill()

    teclas = pygame.key.get_pressed()
    mago.direita = False
    mago.esquerda = False
    if teclas [K_d]:
        mago.direita = True
        mago.virado_para_direita = True
    elif teclas [K_a]:
        mago.esquerda = True
        mago.virado_para_direita = False

    todas_sprites.draw(tela)
    pygame.display.flip()
    todas_sprites.update()
