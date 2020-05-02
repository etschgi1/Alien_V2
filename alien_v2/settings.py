import pygame


class Settings:
    """Class for the game settings"""

    def __init__(self):
        """Initialize settings"""
        # Screen:
        self.screen_width = 1200
        self.screen_height = 800
        self.bgc = (87, 210, 255)
        # ship speed
        self.ship_speed = 1.3
        # upper ship movement limit higher factor means ship cant move that far up
        self.ship_up_bound = self.screen_height*0.95
        # allow up down movement
        self.up_down = True
        # pygame icon
        self.icon = pygame.image.load('images/icon.bmp')
        pygame.display.set_icon(self.icon)

        # Bullets
        self.bullet_speed = 1.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (20, 20, 20)
        self.bullet_damage = 10
