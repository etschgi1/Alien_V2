import pygame
import sys


class DisplayTest():
    """Displays keyinput"""

    def __init__(self):
        """initialise window"""
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        self.screen.get_rect()
        pygame.display.set_caption("Test Keystrokes")
        # init font
        # print("--------------")
        # print(pygame.font.match_font('calibri')) search for font dir
        # print("--------------")
        self.font = pygame.font.Font('C:\Windows\Fonts\calibril.ttf', 30)
        self.text = self.font.render("Test", True, (255, 255, 255))
        self.textRect = self.text.get_rect()
        self.textRect.center = (50, 50)

    def testkeys(self):
        print("start")
        while True:
            # check events
            self._check_press()
            # update screen
            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text, self.textRect)
            pygame.display.flip()

    def _check_press(self):
        """Registers Keypress"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_q:
                print(pygame.event.event_name(event.type))
                sys.exit()
            if event:
                # get the type of event such as keydown or keyup
                text = pygame.event.event_name(event.type)
                text2 = ""
                if event.type == pygame.KEYDOWN:
                    # get the ascii name of pressed key
                    text2 = pygame.key.name(event.key)
                print(text)
                # display as text
                self.text = self.font.render(
                    text+" -  "+text2, False, (255, 255, 255))


if __name__ == '__main__':
    # Make a instance and run
    test = DisplayTest()
    test.testkeys()
