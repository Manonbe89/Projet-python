import pygame
import sys
from Code.item.item import Item

pygame.init()   #initialisation de pygame


class Consumable_Item (Item):
    def __init__(self, id, name, usage, description, picture):
        self.id = id
        self.name = name
        self.usage = usage
        self.description = description
        self.picture = picture
        self.font = pygame.font.Font(None, 32)

    def _Use_consumable_Item(self, screen, item):
        if item.dialogue_step == 1 :
                    screen.blit(self.font.render("Vous utilisez : " + item._get_Name(), True, (255, 255, 255)), (300, 200))  #affiche le texte
                    item._show_passage_text(1, screen, self.font)

        elif item.dialogue_step == 2 :
            
            screen.blit(self.font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
            item._show_passage_text(1, screen, self.font) 
            self._apply_effect(item)

        elif item.dialogue_step >= 3 :
            item.dialogue_step = 0
            item.use_item = False

    def _apply_effect(self, item) :

        if item.use_item == False : 
            if item._get_Name() == "potion" :
                  item.use_item = True

            if item._get_Name() == "bombe" :
                  item.use_item = True