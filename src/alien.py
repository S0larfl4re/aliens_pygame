import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Class to manage alien ships in the game."""

    def __init__(self, ai_game):
        """Initialize the alien and set it's starting position"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Loading alien image and settings it's rect attribute.
        self.image = pygame.image.load("game_assets/alien/alien3.PNG")
        self.rect = self.image.get_rect()

        # Start each new alien  the top left of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # store the aliens exact horizontal position
        self.x = float(self.rect.x)
