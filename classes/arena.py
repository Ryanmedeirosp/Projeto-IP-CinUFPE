import json
import pygame
from constants import ASSETS, MAP_SIZE

class Arena:
    def __init__(self):
        self.image = pygame.image.load(str(ASSETS / 'arena.png')).convert()
        with open(ASSETS / 'arena_walls.json', encoding='utf-8') as file:
            self.walls = [pygame.Rect(*wall) for wall in json.load(file)]
        self.bounds = pygame.Rect(0, 0, MAP_SIZE, MAP_SIZE)

    def collides(self, rect):
        return not self.bounds.contains(rect) or rect.collidelist(self.walls) != -1

    def draw(self, surface):
        surface.blit(self.image, (0, 0))
