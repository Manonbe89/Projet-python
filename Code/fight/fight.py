import pygame
from Code.fight.fight_menu import Fight_Menu

class Fight : 

    def __init__(self, entities, allies_nb):
        self.entities = entities
        self.background_image = pygame.image.load('Images/fight_background.jpg').convert_alpha()
        self.allies = entities[:allies_nb]
        self.enemys = entities[allies_nb:]
        self.menus = []
        for ally in self.allies:
            self.menus.append(Fight_Menu(ally))

    def _handle_event(self, event):
        for menu in self.menus:
            menu._handle_event(event)

    def _draw(self, screen):
        screen.blit(self.background_image, (0,0))
        for i, ally in enumerate(self.allies):
            screen.blit(ally._get_sprite(), (100*(i+1),100*(i+1)))

        for i, enemy in enumerate(self.enemys):
            screen.blit(enemy._get_sprite(), (800*(i+1),100*(i+1)))

        for menu in self.menus:
            menu._draw(screen)

        