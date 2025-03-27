import pygame.image
from pygame import Surface, Rect
from pygame.font import Font

MENU_OPTION = ('LEVEL 1',
               'SCORE',
               'EXIT')

WIN_WIDTH = 576
WIN_HEIGHT = 324


class Menu:
    def __init__(self, window):
        self.window = window

        try:
            self.surf = pygame.image.load('./assets/MenuBg.png').convert_alpha()
        except pygame.error as e:
            print(f"Erro ao carregar a imagem: {e}")
            pygame.quit()
            raise SystemExit

        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0

        try:
            pygame.mixer_music.load('./assets/Menu.mp3')
            pygame.mixer_music.play(-1)
        except pygame.error as e:
            print(f"Erro ao carregar a música: {e}")

        clock = pygame.time.Clock()

        while True:
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(50, "Tank", (229, 255, 204), ((WIN_WIDTH / 2), 70))
            self.menu_text(50, "Shooter", (229, 255, 204), ((WIN_WIDTH / 2), 120))

            for i, option in enumerate(MENU_OPTION):
                color = (178, 255, 102) if i == menu_option else (255, 255, 255)
                self.menu_text(20, option, color, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        menu_option = (menu_option + 1) % len(MENU_OPTION)

                    if event.key == pygame.K_UP:
                        menu_option = (menu_option - 1) % len(MENU_OPTION)

                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

            clock.tick(60)

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

