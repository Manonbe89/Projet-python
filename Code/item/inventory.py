#import Equipement
import pygame
import sys
from Code.item.item import Item

class Inventory:
    def __init__(self):
        self.stuff = [] 
        self.consumable_Item = []
        self.usable_Item = []
        self.image = pygame.image.load('C:/Users/manon/Documents/Projet python S4/Frames/Inventaire_test.png').convert_alpha() #permet d'afficher l'image
        self.open_inventory = False
        self.x = 175   
        self.y = 100                  #coordonnées de l'inventaire
        self.current_item = 0

        #Pour les boutons cliquables :
        self.status_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.buttons = []
        #Première rangée
        for i in range (4) :                         
            x = 22 + i*63                                                           #avec 63 l'ecrt entre 2 cases
            self.buttons.append(pygame.Rect(self.x + x, self.y + 58, 45, 45))        #création de boutons cliquables
        #Deuxième rangée
        for i in range (8) :                         
            x = 22 + i*63
            self.buttons.append(pygame.Rect(self.x + x, self.y + 164, 45, 45))        #création de boutons cliquables
        #Troisième rangée
        for i in range (8) :                         
            x = 22 + i*63
            self.buttons.append(pygame.Rect(self.x + x, self.y + 227, 45, 45))        #création de boutons cliquables

#getters
    def _get_stuff(self):
        return self.stuff
    
    def _get_consumable_Item(self):
        if 0 <= self.current_item < len(self.consumable_Item):
            return self.consumable_Item[self.current_item]
        else :
            return self.consumable_Item[0]      #a enlever quand tt les items seront entrés

    def _get_usable_Item(self):
        return self.usable_Item
    
    def _get_current_Item(self) : 
        return self.current_item
    
    def _get_state(self) :
        return self.open_inventory
    
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

    def _display_inventory(self, screen, font):
        if self.open_inventory : 
            screen.blit(self.image, (self.x, self.y))                     #affiche l'écran d'inventaire

            if 0 <= self.current_item < len(self.consumable_Item):
                if self.status_buttons[self.current_item - 1] :
                    item = self.consumable_Item[self.current_item]
                    item._set_Name(self.consumable_Item[self.current_item]._get_Name())
                    screen.blit(item._get_Picture(), (self.x + 373, self.y + 65))
                    screen.blit(font.render(item._get_Description(), True, (0, 0, 0)), (self.x + 10, self.y + 330))

    def _check_buttons(self, event) :
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].collidepoint(event.pos):
                self.status_buttons = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 1
            elif self.buttons[1].collidepoint(event.pos):
                self.status_buttons = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 2
            elif self.buttons[2].collidepoint(event.pos):
                self.status_buttons = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 3
            elif self.buttons[3].collidepoint(event.pos):
                self.status_buttons = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 4
            elif self.buttons[4].collidepoint(event.pos):
                self.status_buttons = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 5
            elif self.buttons[5].collidepoint(event.pos):
                self.status_buttons = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 6
            elif self.buttons[6].collidepoint(event.pos):
                self.status_buttons = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 7
            elif self.buttons[7].collidepoint(event.pos):
                self.status_buttons = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 8
            elif self.buttons[8].collidepoint(event.pos):
                self.status_buttons = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
                self.current_item = 9

    def _item_factory(self) :
        rien = Item(0, "rien", "Vous ne faites rien", "", "")
        self._set_consumable_Item(rien)
        epee_du_voyageur = Item(1, "epee du voyageur", "Vous gagnez 5 points d'attaque", "L'épée parfaite pour commencer une aventure", "Images/epee_2.png")
        self._set_consumable_Item(epee_du_voyageur)
        rien = Item(0, "rien", "Vous ne faites rien", "", "")
        self._set_consumable_Item(rien)
        rien = Item(0, "rien", "Vous ne faites rien", "", "")
        self._set_consumable_Item(rien)
        rien = Item(0, "rien", "Vous ne faites rien", "", "")
        self._set_consumable_Item(rien)
        potion = Item(2, "potion", "A voir", "Ce breuvage augmente considérablement la (statistique) de son utilisateur", "Images/potion_2.png")
        self._set_consumable_Item(potion)
        bracelet_de_force = Item(3, "bracelet de force", "A voir", "Avec ça plus aucun rocher ne vous résistera", "Images/bracelet de force_2.png")
        self._set_consumable_Item(bracelet_de_force)
        vieux_grimoire = Item(4, "vieux grimoire", "Vous gagnez 5 points de magie", "Le grimoire d'un magicien en herbe", "Images/Grimoire magique_2.png")
        self._set_consumable_Item(vieux_grimoire)
        bombe = Item(5, "bombe", "A voir", "Attention à n'exploser personne", "Images/bombe_2.png")
        self._set_consumable_Item(bombe)



