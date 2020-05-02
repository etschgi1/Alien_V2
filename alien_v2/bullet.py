from settings import Settings


class Bullet():
    """A Class that models bullets from spaceship
    """

    def __init__(self, ai_game):
        """initialize Bullets (size, speed, damage)
        """
        self.settings = ai_game.settings

        self.bullet_width = Settings.bullet_size[0]
        print(self.bullet_width)
