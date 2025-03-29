import pygame
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name: str, game_mode: str, player_score: list[int]):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []

        # Garantir que get_entity retorna uma lista
        entity = EntityFactory.get_entity('Level1Bg')
        if isinstance(entity, list):
            self.entity_list.extend(entity)
        elif entity is not None:
            self.entity_list.append(entity)

    def run(self, player_score: list[int]):
        # Carregar e reproduzir música de fundo
        try:
            pygame.mixer.music.load(f'./assets/{self.name}.mp3')
            pygame.mixer.music.set_volume(0.3)
            pygame.mixer.music.play(-1)
        except pygame.error as e:
            print(f"Erro ao carregar a música: {e}")

        clock = pygame.time.Clock()

        running = True
        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Atualizar e desenhar entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.update()

        pygame.mixer.music.stop()
        pygame.quit()
