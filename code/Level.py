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
        else:
            self.entity_list.append(entity)

    def run(self):
        running = True
        clock = pygame.time.Clock()

        while running:
            # Lidar com eventos do Pygame
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Atualizar e desenhar entidades
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()

            pygame.display.update()

            # Controlar a taxa de quadros (ex: 60 FPS)
            clock.tick(60)

        pygame.quit()
