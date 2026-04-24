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
        self.status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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

            if self.status[0] == True :
                screen.blit(self.image_epee, (self.x + 373, self.y + 65))
                item._set_Name("epee du voyageur")
                screen.blit(font.render("L'épée parfaite pour commencer une aventure", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status[1] == True :
                screen.blit(font.render("Bouton 2 ok", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status[2] == True :
                screen.blit(font.render("Bouton 3 ok", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status[3] == True :
                screen.blit(font.render("Bouton 4 ok", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status[4] == True :
                screen.blit(self.image_potion, (self.x + 373, self.y + 65))
                item._set_Name("potion")
                screen.blit(font.render("Ce breuvage augmente considérablement la \n (statistique) de son utilisateur", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status[5] == True :
                screen.blit(self.image_bracelet, (self.x + 373, self.y + 65))
                item._set_Name("bracelet de force")
                screen.blit(font.render("Avec ça plus aucun rocher ne vous résistera", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status[6] == True :
                screen.blit(self.image_grimoire, (self.x + 373, self.y + 65))
                item._set_Name("vieux grimoire")
                screen.blit(font.render("Le grimoire d'un magicien en herbe", True, (0, 0, 0)), (self.x + 10, self. y + 330))

            elif self.status[7] == True :
                screen.blit(font.render("Bouton 8 ok", True, (0, 0, 0)), (self.x + 10, self. y + 330))


    def _check_buttons(self, event) :
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.buttons[0].collidepoint(event.pos):
                self.status = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif self.buttons[1].collidepoint(event.pos):
                self.status = [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif self.buttons[2].collidepoint(event.pos):
                self.status = [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif self.buttons[3].collidepoint(event.pos):
                self.status = [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif self.buttons[4].collidepoint(event.pos):
                self.status = [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif self.buttons[5].collidepoint(event.pos):
                self.status = [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif self.buttons[6].collidepoint(event.pos):
                self.status = [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif self.buttons[7].collidepoint(event.pos):
                self.status = [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
            elif self.buttons[8].collidepoint(event.pos):
                self.status = [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
