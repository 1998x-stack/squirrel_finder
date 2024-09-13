# entity.py

import pygame
import random
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Entity(pygame.sprite.Sprite):
    """Generic class for player and enemies (strawberries and squirrel)."""
    def __init__(self, image, delay=0):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.height)
        self.speed_x = random.choice([-3, -2, -1, 1, 2, 3])
        self.speed_y = random.choice([-3, -2, -1, 1, 2, 3])
        self.delay = delay  # Delay in seconds before appearing
        self.spawn_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if self.delay > 0:
            if (current_time - self.spawn_time) < self.delay * 1000:
                return  # Do not move until delay has passed

        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Bounce off walls
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.speed_x *= -1
        if self.rect.top <= 0 or self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y *= -1