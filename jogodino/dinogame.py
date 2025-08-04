import pygame
from pygame.locals import *
from sys import exit
import os

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

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauro = []
        for i in range(3):
            img = self.img1 = sprite_sheat.subsurface((i * 32,0),(32,32))
            img = pygame.transform.scale(img,(32*3, 32*3))
            self.imagens_dinossauro.append(img)
        self.index_lista = 0
        self.image = self.imagens_dinossauro[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100,altura - 90)
    def update(self):
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
        self.rect.center = (100,100)
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= 10

todas_as_sprites = pygame.sprite.Group()
dino = Dino()
todas_as_sprites.add(dino)

nuven = Nuvens()
todas_as_sprites.add(nuven)

relogio = pygame.time.Clock()

while True:
    relogio.tick(30)
    tela.fill(branco)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    todas_as_sprites.draw(tela)
    todas_as_sprites.update()

    pygame.display.flip()


