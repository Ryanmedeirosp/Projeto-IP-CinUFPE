import math
import pygame
from constants import PLAYER_SIZE, PLAYER_SPEED

class Player(pygame.sprite.Sprite):
    def __init__(self, position, color, controls):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=position)
        self.position = pygame.Vector2(self.rect.topleft)
        self.controls = controls
        self.speed = PLAYER_SPEED

    def update(self, keys, dt, arena):
        up, down, left, right = self.controls
        direction = pygame.Vector2(int(keys[right])-int(keys[left]),
                                   int(keys[down])-int(keys[up]))
        if direction.length_squared() > 0:
            direction = direction.normalize()
        movement = direction * self.speed * dt
        # Small steps avoid crossing thin walls even during a slow frame.
        steps = max(1, math.ceil(max(abs(movement.x), abs(movement.y)) / 4))
        for _ in range(steps):
            self.move_axis(movement.x / steps, 0, arena)
            self.move_axis(0, movement.y / steps, arena)

    def move_axis(self, dx, dy, arena):
        candidate = self.position + pygame.Vector2(dx, dy)
        rect = self.rect.copy()
        rect.topleft = (round(candidate.x), round(candidate.y))
        if not arena.collides(rect):
            self.position = candidate
            self.rect = rect
