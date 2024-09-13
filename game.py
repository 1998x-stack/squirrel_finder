# game.py

import pygame
from player import Player
from entity import Entity
from config import *
from logger import log_event

class Game:
    """Game class to handle the state, logic, and display."""
    def __init__(self, player_img, strawberry_img, squirrel_img, win_sound, lose_sound, font, screen):
        self.state = 'start'
        self.all_sprites = pygame.sprite.Group()
        self.strawberries = pygame.sprite.Group()
        self.squirrel_group = pygame.sprite.Group()
        self.player = Player(player_img)
        self.all_sprites.add(self.player)
        self.start_time = 0
        self.timer = 0
        self.last_strawberry = 0
        self.squirrel_spawned = False
        self.win = False
        self.lose = False
        self.player_img = player_img
        self.strawberry_img = strawberry_img
        self.squirrel_img = squirrel_img
        self.win_sound = win_sound
        self.lose_sound = lose_sound
        self.font = font
        self.screen = screen

    def reset(self):
        """Resets the game to the initial state."""
        self.state = 'start'
        self.all_sprites.empty()
        self.strawberries.empty()
        self.squirrel_group.empty()
        self.player = Player(self.player_img)
        self.all_sprites.add(self.player)
        self.start_time = pygame.time.get_ticks()
        self.timer = 0
        self.last_strawberry = pygame.time.get_ticks()
        self.squirrel_spawned = False
        self.win = False
        self.lose = False
        log_event("Game reset")

    def spawn_strawberry(self):
        """Spawns a new strawberry on the screen."""
        if len(self.strawberries) < MAX_STRAWBERRIES:
            strawberry = Entity(self.strawberry_img)
            self.all_sprites.add(strawberry)
            self.strawberries.add(strawberry)

    def spawn_squirrel(self):
        """Spawns the squirrel after a delay."""
        squirrel = Entity(self.squirrel_img)
        self.all_sprites.add(squirrel)
        self.squirrel_group.add(squirrel)

    def run(self):
        """Main game loop."""
        CLOCK = pygame.time.Clock()
        running = True

        while running:
            CLOCK.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if self.state == 'start':
                    if event.type == pygame.KEYDOWN:
                        self.state = 'playing'
                        self.start_time = pygame.time.get_ticks()
                        self.last_strawberry = pygame.time.get_ticks()
                        log_event("Game started")

            keys_pressed = pygame.key.get_pressed()

            if self.state == 'playing':
                self.all_sprites.update()
                self.player.handle_keys(keys_pressed)

                current_time = pygame.time.get_ticks()
                if (current_time - self.last_strawberry) >= 1000:
                    self.spawn_strawberry()
                    self.last_strawberry = current_time

                if not self.squirrel_spawned and (current_time - self.start_time) >= 3000:
                    self.spawn_squirrel()
                    self.squirrel_spawned = True

                self.timer = (current_time - self.start_time) // 1000

                if pygame.sprite.spritecollideany(self.player, self.strawberries):
                    self.state = 'lose'
                    self.lose = True
                    pygame.mixer.Sound.play(self.lose_sound)
                    pygame.time.set_timer(pygame.USEREVENT + 1, 2000)
                    log_event("Player lost the game")

                if pygame.sprite.spritecollideany(self.player, self.squirrel_group):
                    self.state = 'win'
                    self.win = True
                    pygame.mixer.Sound.play(self.win_sound)
                    pygame.time.set_timer(pygame.USEREVENT + 2, 2000)
                    log_event("Player won the game")

            elif self.state in ['win', 'lose']:
                for event in pygame.event.get():
                    if event.type == pygame.USEREVENT + 1 and self.lose:
                        self.reset()
                    if event.type == pygame.USEREVENT + 2 and self.win:
                        self.reset()

            self.screen.fill(BLACK)

            if self.state == 'start':
                instructions = [
                    "Welcome to Squirrel Finder!",
                    "Use the arrow keys to move the koala.",
                    "Avoid the bouncing strawberries.",
                    "Catch the squirrel to win.",
                    "Press any key to start."
                ]
                for idx, line in enumerate(instructions):
                    text = self.font.render(line, True, WHITE)
                    self.screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 2 - 100 + idx * 40))
            else:
                self.all_sprites.draw(self.screen)
                openai_text = self.font.render("openai", True, RETRO_GREEN)
                self.screen.blit(openai_text, (10, 10))
                timer_text = self.font.render(f"Time: {self.timer}s", True, WHITE)
                self.screen.blit(timer_text, (SCREEN_WIDTH - 150, 10))

                if self.state == 'win':
                    win_text = self.font.render("You Win!", True, RETRO_GREEN)
                    self.screen.blit(win_text, (SCREEN_WIDTH // 2 - win_text.get_width() // 2, SCREEN_HEIGHT // 2))
                elif self.state == 'lose':
                    lose_text = self.font.render("You Lost!", True, RETRO_RED)
                    self.screen.blit(lose_text, (SCREEN_WIDTH // 2 - lose_text.get_width() // 2, SCREEN_HEIGHT // 2))

            pygame.display.flip()

        pygame.quit()