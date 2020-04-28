import pygame


class Ship():
    """Manages the ship"""

    def __init__(self, ai_game):
        """initialize ship and set starting pos"""
        self.screen = ai_game.screen
        # ship settings
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Load the ship image and get ist rect
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        # Start each new ship at the bottom center of the screen
        self.rect.midbottom = self.screen_rect.midbottom

        # setting initial x and y pos
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        # setting initial flags for movement to false
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        """Update the ship's position based on the movment flag."""
        # uptade float for excat position
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > self.screen_rect.top+self.settings.ship_up_bound:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed
        # uptade actual position of rect obj
        self.rect.x = self.x
        self.rect.y = self.y
