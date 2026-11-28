import pygame
from constants import LARGURA, ALTURA
pygame.init()
tela = pygame.display.set_mode((LARGURA, ALTURA))
from classes.game import Game

jogo = Game()
jogo.executar()

pygame.quit()