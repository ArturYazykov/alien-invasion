import pygame
from pygame.sprite import Sprite


class Alien(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.scrin = ai_game.screen
        self.settings = ai_game.settings

        self.image = pygame.image.load('images/alian_stalin.png')
        self.image = pygame.transform.scale(self.image, (
            self.settings.alien_width,
            self.settings.alien_height
        ))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)