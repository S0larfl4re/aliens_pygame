import pygame


class Ship:
    """A class to manage the ship."""

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings
        # Load the ship's image and get it's rect.
        alpha = 0
        self.image = pygame.image.load(
            "game_assets/space_ship/stealth_bomber.png"
        ).convert_alpha()
        print(self.image)
        self.rect = self.image.get_rect()
        # Initialize each ship at middle of the bottom of the screen.
        self.rect.midbottom = self.screen_rect.midbottom
        # store a float for ships's exact X axis position

        self.x = float(self.rect.x)
        self.move_right = False
        self.move_left = False

    def update(self):
        """Update the ship's position based on movement flag"""
        if self.move_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.move_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed

        self.rect.x = self.x

    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image, self.rect)
