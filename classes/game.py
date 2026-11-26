import pygame
from constants import FPS, MAP_SIZE, WINDOW_SIZE
from classes.arena import Arena
from classes.player import Player

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))
        pygame.display.set_caption('Arena PvP - Projeto IP')
        self.world = pygame.Surface((MAP_SIZE, MAP_SIZE))
        self.clock = pygame.time.Clock()
        self.arena = Arena()
        self.players = pygame.sprite.Group(
            Player((128, 440), (45, 155, 255), (pygame.K_w, pygame.K_s, pygame.K_a, pygame.K_d)),
            Player((1138, 477), (255, 65, 75), (pygame.K_UP, pygame.K_DOWN, pygame.K_LEFT, pygame.K_RIGHT))
        )
        self.running = True

    def run(self):
        while self.running:
            dt = min(self.clock.tick(FPS) / 1000, 0.1)
            for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    self.running = False
            self.players.update(pygame.key.get_pressed(), dt, self.arena)
            self.arena.draw(self.world)
            self.players.draw(self.world)
            self.screen.blit(pygame.transform.smoothscale(self.world, self.screen.get_size()), (0, 0))
            pygame.display.flip()
        pygame.quit()
