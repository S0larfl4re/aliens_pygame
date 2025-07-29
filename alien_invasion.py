import sys
from ship import Ship
from settings import Settings
import pygame

class AlienInvasion :


	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.init()
		self.settings = Settings()
		self.clock = pygame.time.Clock()
		self.screen = pygame.display.set_mode((self.settings.screen_width ,\
							self.settings.screen_height))
		pygame.display.set_caption("Alien_Invasion!")
		self.ship = Ship(self)


	def _check_events(self):
		for event in pygame.event.get():
			print(event)
			if event.type == pygame.QUIT:
				sys.exit()
			
			if event.type == pygame.TEXTINPUT:
				if event.text == 'l':
					self.ship.rect.x += 1

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()	


	def run_game(self):
		"""Start main loop of the game"""
		while True:
			
			self._check_events()			
			self._update_screen()
			pygame.display.flip()
			self.clock.tick(60)


if __name__ == '__main__':
# Make a game instance and run the game.

	ai = AlienInvasion()

	ai.run_game()
