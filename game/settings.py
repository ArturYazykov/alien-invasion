class Settings:
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (250, 50, 150)


        # Настройки корабля
        self.ship_speed = 5

        # Параметры снаряда
        self.bullet_speed = 3
        self.bullet_width = 167
        self.bullet_height = 100
        self.bullet_img_path = 'images/bullet.png'
        self.bullets_allowed = 7

        self.alien_width = 70
        self.alien_height = 80


