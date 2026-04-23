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
        self.x = 175   
        self.y = 100                  #coordonnées de l'inventaire

        #Pour les boutons cliquables :
        self.button_1 = pygame.Rect(self.x + 22, self.y + 58, 45, 45)
        self.status_1 = False
        self.button_5 = pygame.Rect(self.x + 22, self.y + 164, 45, 45)           #crée un bouton cliquable
        self.status_5 = False
        self.button_6 = pygame.Rect(self.x + 85, self.y + 164, 45, 45)           #crée un bouton cliquable
        self.status_6 = False

        #Pour les images :
        self.image_epee = pygame.image.load("Images/epee_2.png").convert_alpha()
        self.image_potion = pygame.image.load("Images/potion_2.png").convert_alpha()
        self.image_bracelet = pygame.image.load("Images/bracelet de force_2.png").convert_alpha()
        self.image_grimoire = pygame.image.load("Images/Grimoire magique_2.png").convert_alpha()

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

    def _display_inventory(self, screen, item, font):
        if self.open_inventory == True : 
            screen.blit(self.image, (self.x, self.y))                     #affiche l'écran d'inventaire
            if self.status_1 == True :
                screen.blit(self.image_epee, (self.x + 373, self.y + 65))
                item._set_Name("epee du voyageur")
                screen.blit(font.render("L'épée parfaite pour commencer une aventure", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status_5 == True :
                screen.blit(self.image_bracelet, (self.x + 373, self.y + 65))
                item._set_Name("bracelet de force")
                screen.blit(font.render("Avec ça plus aucun rocher ne vous résistera", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status_6 == True :
                screen.blit(self.image_grimoire, (self.x + 373, self.y + 65))
                item._set_Name("vieux grimoire")
                screen.blit(font.render("Le grimoire d'un magicien en herbe", True, (0, 0, 0)), (self.x + 10, self. y + 330))


    def _check_buttons(self, event) :
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.button_1.collidepoint(event.pos):
                self.status_1 =True
                print("Le bouton a été cliqué !")
                self.status_5 = False
                self.status_6 = False
            elif self.button_5.collidepoint(event.pos):
                self.status_5 =True
                print("Le bouton a été cliqué !")
                self.status_1 = False
                self.status_6 = False
            elif self.button_6.collidepoint(event.pos):
                self.status_6 =True
                print("Le bouton a été cliqué !")
                self.status_1 = False
                self.status_5 = False
