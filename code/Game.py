import sys

import pygame

from code.Level import Level
from code.Menu import Menu

MENU_OPTION = ('LEVEL 1',
               'SCORE',
               'EXIT')

WIN_WIDTH = 576
WIN_HEIGHT = 324


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                player_score = [0, 0]
                level = Level(self.window, 'Level 1', menu_return, player_score)
                level.run(player_score)

            elif menu_return == MENU_OPTION[1]:
                pass

            elif menu_return == MENU_OPTION[2]:
                pygame.quit()
                sys.exit()
