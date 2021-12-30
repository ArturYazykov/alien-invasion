import pygame


class Ekran:
    def __init__(self, ai_game):
        super().__init__()
        self.image = pygame.image.load('images/edinorog.bmp')
        self.image.draw(self.screen)
