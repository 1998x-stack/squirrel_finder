# main.py

import pygame
from game import Game
from config import *
from logger import log_event

# Initialize pygame
pygame.init()

# Set up screen and font
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Squirrel Finder")
FONT = pygame.font.SysFont('arial', FONT_SIZE)

# Load assets
PLAYER_IMG = pygame.image.load(KOALA_IMG_PATH)
PLAYER_IMG = pygame.transform.scale(PLAYER_IMG, (40, 40))

STRAWBERRY_IMG = pygame.image.load(STRAWBERRY_IMG_PATH)
STRAWBERRY_IMG = pygame.transform.scale(STRAWBERRY_IMG, (40, 40))

SQUIRREL_IMG = pygame.image.load(SQUIRREL_IMG_PATH)
SQUIRREL_IMG = pygame.transform.scale(SQUIRREL_IMG, (40, 40))

# Load sounds
WIN_SOUND = pygame.mixer.Sound(WIN_SOUND_PATH)
LOSE_SOUND = pygame.mixer.Sound(LOSE_SOUND_PATH)

# Log game initialization
log_event("Game initialized")

# Start the game
if __name__ == "__main__":
    game = Game(PLAYER_IMG, STRAWBERRY_IMG, SQUIRREL_IMG, WIN_SOUND, LOSE_SOUND, FONT, SCREEN)
    game.run()