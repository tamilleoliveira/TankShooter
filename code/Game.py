import pygame

from code.Menu import Menu


class Game:
    def __init__(self):
        self.window = None

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
