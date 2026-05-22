import pygame

class Fight : 

    def __init__(self, *entity, allies_nb):
        self.entity = entity
        self.allies
        self.enemys
        self.background_image = pygame.image.load('Images/fight_background')
        for i in allies_nb:
            self.allies = entity[i]
        for i+allies_nb in entity.count:
            self.enemys = entity[i]
        self

    def _draw(self, screen):
        screen.blit(self.background_image, (0,0))
        for i in self.allies.count:
            screen.blit(self.allies[i].get_sprite, (200*(i+1),100*(i+1)))

        for i in self.enemys.count:
            screen.blit(self.enemys[i].get_sprite, (800*(i+1),100*(i+1)))

        