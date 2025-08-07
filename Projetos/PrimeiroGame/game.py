import pygame
from pygame.locals import *
from sys import exit
import os

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


fundo = pygame.image.load(os.path.join(diretorio_imagens,'floresta.png'))
tela_de_fundo = pygame.transform.scale(fundo,(largura,altura))

pygame.display.set_caption('Mago')

relogio = pygame.time.Clock()

class Mago(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.virado_para_direita = True
        self.direita = False
        self.esquerda = False
        self.pulando = False
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
        self.index_sprite = 0
        self.image = self.spritesparado[self.index_sprite]
        self.rect = self.image.get_rect()
        self.rect.x = 300
        self.rect.y = self.altura_inicial

    def update(self):
        if self.pulando:
            if self.rect.y > 350:
                self.rect.y -= velocidade_pulo
            else:
                self.pulando = False
        if self.pulando == False and self.rect.y < self.altura_inicial:
            self.rect.y += velocidade_pulo

        if self.direita:
            if self.index_sprite > 7:
                self.index_sprite = 0
            self.rect.x += velocidade
            self.image = self.correrdireita[int(self.index_sprite)]
            self.index_sprite += 0.3
        elif self.esquerda:
            if self.index_sprite > 7:
                self.index_sprite = 0
            if self.rect.x > -20:
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

todas_sprites = pygame.sprite.Group()
mago = Mago()
todas_sprites.add(mago)

while True:
    relogio.tick(30)
    tela.blit(tela_de_fundo,(0,0))
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    teclas = pygame.key.get_pressed()

    mago.direita = False
    mago.esquerda = False
    if teclas [K_d]:
        mago.direita = True
        mago.virado_para_direita = True
    elif teclas [K_a]:
        mago.esquerda = True
        mago.virado_para_direita = False
    if teclas [K_w] or teclas [K_SPACE]:
        mago.pulando = True
    

    todas_sprites.draw(tela)
    pygame.display.flip()
    todas_sprites.update()
