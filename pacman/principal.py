import pygame
from constantes import *
import sprites
import os


class Game:
    def __init__(self):
        #criando a tela do jogo
        pygame.init()
        pygame.mixer.init()
        self.tela = pygame.display.set_mode((LARGURA,ALTURA))
        pygame.display.set_caption(TITULO_JOGO)
        self.relogio = pygame.time.Clock()
        self.esta_rodando = True
        self.fonte = pygame.font.match_font(FONTE)
        self.carregar_arquivos()
    def novo_jogo(self):
        #instancia as classes das sprites do jogo
        self.todas_as_sprites = pygame.sprite.Group()
        self.rodar()
    def rodar(self):
        #loop do jogo
        self.jogando = True
        while self.jogando:
            self.relogio.tick(FPS)
            self.eventos()
            self.atualizar_sprites()
            self.desenhar_sprites()

    def eventos(self):
        #Define os eventos do jogo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if self.jogando:
                    self.jogando = False
                self.esta_rodando = False

    def atualizar_sprites(self):
        #atualizar sprites
        self.todas_as_sprites.update()

    def desenhar_sprites(self):
        #Desenhar sprites
        self.tela.fill((PRETO)) #Limpando a tela
        self.todas_as_sprites.draw(self.tela) #Desenhando as sprites
        pygame.display.flip() #Atualiza a tela

    def carregar_arquivos(self):
        #Carregar os arquivos de audios e imagens
        
        # Base do diretório onde está o script
        base_dir = os.path.dirname(__file__)
        
        # Pastas
        self.diretorio_imagens = os.path.join(base_dir, 'imagens')
        self.diretorio_audios = os.path.join(base_dir, 'audios')
        
        # Arquivos
        self.spritesheet = os.path.join(self.diretorio_imagens, SPRITESHEET)
        self.pacmen_start_logo = os.path.join(self.diretorio_imagens, PACMAN_START_LOGO)
        
        # Carregar imagens
        self.pacmen_start_logo = pygame.image.load(self.pacmen_start_logo).convert()


    def mostrar_texto(self,texto,tamanho,cor,pos_x,pos_y):
        #Exibe um texto na tela do jogo
        fonte = pygame.font.Font(self.fonte,tamanho)
        texto = fonte.render(texto,True,cor)
        texto_rect = texto.get_rect()
        texto_rect.midtop = (pos_x,pos_y)
        self.tela.blit(texto,texto_rect)

    def mostrar_start_logo(self,x,y):
        start_logo_rect = self.pacmen_start_logo.get_rect()
        start_logo_rect.midtop = (x,y)
        self.tela.blit(self.pacmen_start_logo,start_logo_rect)

    def mostrar_tela_start(self):
        pygame.mixer_music.load(os.path.join(self.diretorio_audios,MUSICA_START))
        pygame.mixer.music.play()
        self.mostrar_start_logo(LARGURA//2,20)
        self.mostrar_texto('Pressione uma tecla para jogar', 32, AMARELO, LARGURA//2,320)
        self.mostrar_texto('Desenvolvido por Geovane Bussola', 19, BRANCO, LARGURA//2,570)
        pygame.display.flip()
        self.esperar_por_jogador()

    def esperar_por_jogador(self):
        esperando = True
        while esperando:
            self.relogio.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    esperando = False
                    self.esta_rodando = False
                if event.type == pygame.KEYUP:
                    esperando = False
                    pygame.mixer.music.stop()
                    pygame.mixer.Sound(os.path.join(self.diretorio_audios,TECLA_START)).play()

    def mostrar_tela_game_over(self):
        pass

    


g = Game()
g.mostrar_tela_start()
while g.esta_rodando:
    g.novo_jogo()
    g.mostrar_tela_game_over()
