class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1920
        self.screen_height = 1080
        self.bg_color = (250, 50, 150)
        # self.screen_img_path = 'images/edinorog.bmp'

        # Настройки корабля
        self.ship_speed = 5
        self.ship_limit = 3

        # Параметры снаряда
        self.bullet_speed = 3
        self.bullet_width = 160
        self.bullet_height = 90
        self.bullet_img_path = 'images/bullet.png'
        self.bullets_allowed = 7

        self.alien_width = 70
        self.alien_height = 80

        self.alien_speed = 3
        self.fleet_drop_speed = 20
        self.fleet_direction = 1
