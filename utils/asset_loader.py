import pygame
import os
from constants import PASTA_IMAGENS, PASTA_SONS, PASTA_MUSICAS, LARGURA, ALTURA
pygame.init()
# Moldes de exemplo
# Carregar imagem
imagem_fundo = pygame.image.load(os.path.join(PASTA_IMAGENS, "Labirinto Verde em Pixel Art.png")).convert()
# Carregar som
# som_1 = pygame.mixer.Sound(os.path.join(PASTA_SONS, "som.wav"))

# Carregar musica de fundo
# musica_1 = pygame.mixer.music.load(os.path.join(PASTA_MUSICAS, "musica.mp3"))
