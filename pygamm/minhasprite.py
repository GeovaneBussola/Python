import pygame
from pygame.locals import *
from sys import exit


pygame.init()

largura = 640
altura = 480

preto = (0,0,0)
tela = pygame.display.set_mode((largura,altura))  #tamanho da tela
pygame.display.set_caption('Sprites')  #Titulo da janela


class Personagem(pygame.sprite.Sprite):
    def __init__(self,):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("pygamm/mysprites/sprite1.png"))
        self.sprites.append(pygame.image.load("pygamm/mysprites/sprite2.png"))
        self.sprites.append(pygame.image.load("pygamm/mysprites/sprite3.png"))
        self.sprites.append(pygame.image.load("pygamm/mysprites/sprite4.png"))


        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image,(32*7,32*7))
        self.rect = self.image.get_rect()
        self.rect.topleft = 0,180

    def update(self):
        self.atual += 0.25
        if self.atual >= len(self.sprites):
            self.atual = 0

        self.image = self.sprites[int(self.atual)]
        self.image = pygame.transform.scale(self.image,(32*7,32*7))

imagem_fundo = pygame.image.load("pygamm/mysprites/background.jpg").convert()
imagem_fundo = pygame.transform.scale(imagem_fundo,(640,480))
todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

relogio = pygame.time.Clock()

while True:
    relogio.tick(50)
    tela.fill(preto)  #Desenha tela
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    tela.blit(imagem_fundo,(0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip() #Atualiza a tela (É importante a cada frame)