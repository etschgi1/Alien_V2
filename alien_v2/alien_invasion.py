import sys
import pygame
from settings import Settings
from ship import Ship


class AlienInvasion:

    """Class to manage a individual game"""

    def __init__(self):
        """Initialize the game window / caption ship"""
        pygame.init()  # pygame lib initialize
        # settings init before screen for icon init
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width, self.settings.screen_height = self.screen\
            .get_rect().width, self.screen.get_rect().height
        # ship init after screen because ship needs it to initialize
        self.ship = Ship(self)
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Starts the main game loop"""
        while True:
            # checks for events
            self._check_events()
            # update ship pos
            self.ship.update()
            # update screen
            self._uptade_screen()

    def _check_events(self):
        """Checks for keyboard and mouse events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Checks for Keydown events"""
        # UP DOWN LEFT RIGHT Movement
        if event.key == pygame.K_RIGHT:
            # flag for movement to the right
            self.ship.moving_right = True
        if event.key == pygame.K_LEFT:
            # flag for movement to the left
            self.ship.moving_left = True
        if self.settings.up_down == True:
            if event.key == pygame.K_UP:
                # flag for movement to the right
                self.ship.moving_up = True
            if event.key == pygame.K_DOWN:
                # flag for movement to the left
                self.ship.moving_down = True
        if event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        """Checks for Keyup events"""
        if event.key == pygame.K_RIGHT:
            # flag
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            # flag
            self.ship.moving_left = False
        if self.settings.up_down == True:
            if event.key == pygame.K_UP:
                # flag
                self.ship.moving_up = False
            if event.key == pygame.K_DOWN:
                # flag
                self.ship.moving_down = False

    def _uptade_screen(self):
        """Updates the screen"""
        # display background color set in settings class
        self.screen.fill(self.settings.bgc)
        # display ship
        self.ship.blitme()
        # display most recent screen
        pygame.display.flip()


if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
