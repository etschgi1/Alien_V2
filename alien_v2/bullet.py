import pygame
from pygame.sprite import Sprite


class Bullet():
    """A Class that models bullets from spaceship
    """

    def __init__(self, ai_game):
        """initialize Bullets (size, speed, damage)
        """
        super(Sprite).__init__()  # super init for sprite
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Create Bullet rect and set correct position
        self.rect = pygame.Rect(
            0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store the bullet's position as a decimal value
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet up the screen."""
        # Update dec pos
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw the bullet to the screen"""
        pygame.draw.rect(self.screen, self.color, self.rect)
