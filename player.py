# player.py

import pygame
from entity import Entity
from config import SCREEN_WIDTH, SCREEN_HEIGHT

class Player(Entity):
    """Player class that represents the koala."""
    def __init__(self, image):
        super().__init__(image)
        self.rect.center = (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
        self.speed = 5

    def handle_keys(self, keys_pressed):
        """Handles the player movement via arrow keys."""
        if keys_pressed[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys_pressed[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys_pressed[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys_pressed[pygame.K_DOWN]:
            self.rect.y += self.speed

        # Keep player within screen
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
        self.rect.y = max(0, min(self.rect.y, SCREEN_HEIGHT - self.rect.height))