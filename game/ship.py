import pygame

class Ship():
    """Класс для управления пингвином."""

    def __init__(self, ai_game):
        """Инициализирует пингвина и задает его начальную позицию."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля
        self.image = pygame.image.load('images/ship.png')
        self.rect = self.image.get_rect()
        #
        self.rect.midbottom = self.screen_rect.midbottom

        #
        self.x = float(self.rect.x)

        # Флаги пермещения
        self.moving_right = False
        self.moving_left = False



    def update(self):
        if self.moving_right  and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x


    def blitme(self):
        """Рисует пингвина в текущей позе"""
        self.screen.blit(self.image, self.rect)