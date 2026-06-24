import pygame
from codigo.Const import WIN_WIDTH, WIN_HEIGHT
from codigo.Menu import Menu
from codigo.Level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.window = pygame.display.set_mode(
            (WIN_WIDTH, WIN_HEIGHT)
        )
        pygame.display.set_caption(
            "Space Invaders"
        )
    def run(self):

        menu = Menu(self.window)

        menu.run()

        level = Level(self.window)

        level.run()