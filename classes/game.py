import pygame
from pygame.locals import *
from constants import LARGURA, ALTURA, FPS, TITULO_JOGO
from utils.asset_loader import imagem_fundo
from jogador import Jogador

class Game:
    def __init__(self):
        pygame.init()

        # Tela e tela de fundo
        self.tela = pygame.display.set_mode((LARGURA, ALTURA))
        pygame.display.set_caption(TITULO_JOGO)
        self.fundo = imagem_fundo
        self.clock = pygame.time.Clock()

        # Criação das sprites (so criei os jogadores por enquanto)
        self.jogador1 = Jogador((50, 50), (K_w, K_s, K_a, K_d))
        self.jogador2 = Jogador((560, 400), (K_UP, K_DOWN, K_LEFT, K_RIGHT))
        self.todas_as_sprites = pygame.sprite.Group()
        self.todas_as_sprites.add(self.jogador1, self.jogador2) 
        
        self.rodando = True


    def eventos(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.rodando = False

    def desenhar(self):
        self.tela.blit(self.fundo, (0, 0))
        self.todas_as_sprites.draw(self.tela)
        pygame.display.flip()

    def update(self):
        self.todas_as_sprites.update()

    def executar(self):
        while self.rodando:
            self.eventos()

            if self.rodando:
                self.update()
                self.desenhar()

            self.clock.tick(FPS)
