import pygame.display
import pygame
from pygame.locals import *
from sys import exit
from random import randint,choice
from time import sleep

pygame.init()

largura = 680
altura = 480

tela = pygame.display.set_mode((largura,altura))

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_g:
                tela.fill((0,0,0))
                pygame.display.update
                sleep(3)

    tela.fill((255,255,0))
    pygame.display.update()

