import pygame
from constants import VELOCIDADE_JOGADOR, TAMANHO_JOGADOR

class Jogador(pygame.sprite.Sprite):
    def __init__(self, posicao, controles):
        super().__init__()

        self.controles = controles
        self.velocidade = VELOCIDADE_JOGADOR

        # Imagem criada so para teste (a classe jogador principal não terá imagem)
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))

        self.rect = pygame.Rect(posicao[0], posicao[1], TAMANHO_JOGADOR, TAMANHO_JOGADOR)

    def update(self):
        cima, baixo, esquerda, direita = self.controles
        teclas = pygame.key.get_pressed()

        if teclas[cima]:
            self.rect.y -= self.velocidade
        if teclas[baixo]:
            self.rect.y += self.velocidade
        if teclas[esquerda]:
            self.rect.x -= self.velocidade
        if teclas[direita]:
            self.rect.x += self.velocidade
