import sys
from time import sleep
import pygame

from game.settings import Settings
from game.game_stats import GameStats
from game.ship import Ship
from game.bullet import Bullet
from game.alian import Alien


class AlienInvasion:
    """Класс для управления ресурсами и поведением игры."""

    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы."""
        pygame.init()

        self.settings = Settings()

        # self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        # self.settings.screen_width = self.screen.get_rect().width
        # self.settings.screen_height = self.screen.get_rect().height
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))

        pygame.display.set_caption("Alien Invasion")
        self.stats = GameStats(self)

        # Create Player Ship
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()

        # Create aliens fleet
        self.aliens = pygame.sprite.Group()
        self._create_fleet()

    def _ship_hit(self):
        self.stats.ships_left -= 1

        self.aliens.empty()  #
        self.bullets.empty()

        self._create_fleet()
        self.ship.center_ship()  #

        self.screen.fill((255, 0, 0))
        pygame.display.flip()
        sleep(1.5)
        self.screen.fill(self.settings.bg_color)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        available_space_x = self.settings.screen_width - (2 * alien_width)
        number_aliens_x = available_space_x // (2 * alien_width)

        ship_height = self.ship.rect.height
        available_space_y = self.settings.screen_height - (3 * alien_height) - ship_height
        number_rows = available_space_y // (2 * alien_height)

        for row_number in range(number_rows):
            # Создание первого ряда пришельцев.
            for alien_number in range(number_aliens_x):
                self._create_alien(alien_number, row_number)

        # Создание пришельца и размещение его в ряду.

    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + 2 * alien_width * alien_number
        alien.rect.x = alien.x
        alien.rect.y = alien_height + 2 * alien_height * row_number
        self.aliens.add(alien)

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            print("Ship bo-bo :(")
        self._check_aliens_bottom()

    def _check_aliens_bottom(self):
        screen_rect = self.screen.get_rect()
        for aliens in self.aliens.sprites():
            if aliens.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def run_game(self):
        """Запуск основного цикла игры."""
        while True:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_aliens()
            self.bullets.update()
            self._update_screen()
            # При каждом проходе цикла перерисовывается экран.

    def _update_bullets(self):
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)

        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()

        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed

        self.settings.fleet_direction *= -1

    def _check_events(self):
        # Отслеживание событий клавиатуры и мыши.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_ESCAPE:  # кнопка выхода
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_screen(self):
        """обновляет кадры"""

        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

        self.aliens.draw(self.screen)

        # Отображение последнего прорисованного экрана.
        pygame.display.flip()


if __name__ == '__main__':
    # Создание экземпляра и запуск игры.
    ai = AlienInvasion()
    ai.run_game()
