import pygame


class Settings:
    """A class that stores all setting for alien invasions"""

    def __init__(self):
        """Initialize the game's settings"""
        # Screen Settings

        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        # Ship Settings
        self.ship_speed = 5

        # Bullet Settings
        self.bullet_speed = 7.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bg_picture = pygame.image.load(
            "game_assets/back_ground/white-cloud-blue-sky_scaled.jpg"
        )
