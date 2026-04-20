#import Equipement
import pygame
import sys

class Inventory:
    def __init__(self):
        self.stuff = [] 
        self.consumable_Item = []
        self.usable_Item = []
        self.image = pygame.image.load('C:/Users/manon/Documents/Projet python S4/Frames/Inventaire_test.png').convert_alpha() #permet d'afficher l'image
        self.open_inventory = False

#getters
    def _get_stuff(self):
        return self.stuff
    
    def _get_consumable_Item(self):
        return self.consumable_Item

    def _get_usable_Item(self):
        return self.usable_Item
    
#setters
    def _set_stuff(self, Item):
        self.stuff.append(Item)

    def _set_consumable_Item(self, Item):
        self.consumable_Item.append(Item)

    def _set_usable_Item(self, Item):
        self.usable_Item.append(Item)

    def _check_inventory_status(self, event):
        if event.type == pygame.KEYDOWN :                           # vérifie si l'événement keydown s'est produit ou non
             if event.key == pygame.K_i :                           # vérifie si la touche "i" a été pressée
                self.open_inventory = not self.open_inventory       #inverse l'état de self.open_inventory

    def _display_inventory(self, screen):
        if self.open_inventory == True : 
            screen.blit(self.image, (175, 100))                     #affiche l'écran d'inventaire