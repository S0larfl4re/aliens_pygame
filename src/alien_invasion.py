import sys
from ship import Ship
from settings import Settings
from bullets import Bullet
import pygame

class AlienInvasion :


	def __init__(self):
		"""Initialize the game and create game resources."""
		pygame.init()
		self.settings = Settings()
		self.clock = pygame.time.Clock()
		# self.screen = pygame.display.set_mode((self.settings.screen_width ,\
		# 					self.settings.screen_height))

		self.screen = pygame.display.set_mode((0, 0),pygame.FULLSCREEN)
		self.settings.screen_width = self.screen.get_rect().width
		self.settings.screen_height = self.screen.get_rect().height

		pygame.display.set_caption("Alien_Invasion!")
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()


	def _check_events(self):
		for event in pygame.event.get():

			if event.type == pygame.QUIT:
				sys.exit()
			if event.type == pygame.KEYDOWN:
				self._check_keydown_event(event)
			if event.type == pygame.KEYUP:
				self._check_keyup_event(event)
	
	def _check_keydown_event(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = True
		if event.key == pygame.K_LEFT:
			self.ship.move_left = True
		if event.key == pygame.K_q:
			sys.exit()
		if event.key ==pygame.K_SPACE:
			self._fire_bullet()

	def _check_keyup_event(self, event):
		if event.key == pygame.K_RIGHT:
			self.ship.move_right = False
		if event.key == pygame.K_LEFT:
			self.ship.move_left = False

	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group."""
		new_bullet = Bullet(self)
		self.bullets.add(new_bullet)

	def _update_screen(self):
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()

	def _update_bullets(self):
		"""Update position of  bullets and remove old bullets."""
		self.bullets.update()
		# Remove bullets that have disappeared.
		for bullet in self.bullets.copy():
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)

	def run_game(self):
		"""Start main loop of the game"""
		while True:
			
			self._check_events()			
			self._update_screen()
			self.ship.update()
			self._update_bullets()
			# Redraw the screen during each pass through the loop.
			pygame.display.flip()
			self.clock.tick(75)

			


if __name__ == '__main__':
# Make a game instance and run the game.

	ai = AlienInvasion()

	ai.run_game()
