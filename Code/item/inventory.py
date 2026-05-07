#import Equipement
import pygame
import sys
from Code.item.item import Item

class Inventory:
    def __init__(self):
        self.item = [] 
        self.item_status = [0, 0, 0, 0, 0, 0, 0, 0]
        self.image = pygame.image.load('C:/Users/manon/Documents/Projet python S4/Frames/Inventaire_2.png').convert_alpha() #permet d'afficher l'image
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
    def _get_Item(self):
        if 0 <= self.current_item < len(self.item):
            return self.item[self.current_item]
        else :
            return self.item[0]      #a enlever quand tt les items seront entrés
    
    def _get_current_Item(self) : 
        return self.current_item
    
    def _get_state(self) :
        return self.open_inventory
    
#setters
    def _set_Item(self, Item):
        self.item.append(Item)

    def _set_item_status(self, index) :
        self.item_status[index] = 1

    def _check_inventory_status(self, event):
        if event.type == pygame.KEYDOWN :                           # vérifie si l'événement keydown s'est produit ou non
             if event.key == pygame.K_i :                           # vérifie si la touche "i" a été pressée
                self.open_inventory = not self.open_inventory       #inverse l'état de self.open_inventory

    def _display_inventory(self, screen, font):
        if self.open_inventory : 
            screen.blit(self.image, (self.x, self.y))                     #affiche l'écran d'inventaire

            if 0 <= self.current_item < len(self.item) and self.status_buttons[self.current_item - 1] :
                        item = self.item[self.current_item]
                        item._set_Name(item._get_Name())
                        screen.blit(item._get_Picture(), (self.x + 373, self.y + 65))
                        screen.blit(font.render(item._get_Description(), True, (0, 0, 0)), (self.x + 10, self.y + 330))

    def _check_buttons(self, event) :
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (9) :
                if self.buttons[i].collidepoint(event.pos):
                    self.status_buttons[i] = 1
                    self.current_item = i
                    print("bouton ok :", i)

    def _item_factory(self) :
        rien = Item(0, "rien", "Vous ne faites rien", "", "")
        self._set_Item(rien)
        epee_du_voyageur = Item(1, "epee du voyageur", "Vous gagnez 5 points d'attaque", "L'épée parfaite pour commencer une aventure", "Images/epee_2.png")
        potion = Item(2, "potion", "A voir", "Ce breuvage augmente considérablement la (statistique) de son utilisateur", "Images/potion_2.png")
        bracelet_de_force = Item(3, "bracelet de force", "A voir", "Avec ça plus aucun rocher ne vous résistera", "Images/bracelet de force_2.png")
        bombe = Item(4, "bombe", "A voir", "Attention à n'exploser personne", "Images/bombe_2.png")
        vieux_grimoire = Item(5, "vieux grimoire", "Vous gagnez 5 points de magie", "Le grimoire d'un magicien en herbe", "Images/Grimoire magique_2.png")
        cuirasse = Item(6, "cuirasse", "Vous gagnez 5 points de defense", "Une cuirasse robuste pour résister à n'importe quelle lame", "Images/cuirasse_2.png")
        chapeau_de_magicien = Item(7, "chapeau de magicien", "Vous gagnez 5 points de defense magique", "Ce chapeau aurait appartenu à un valeureux magicien, il vous protègera sûrement du mauvais sort", "Images/chapeau de magicien_2.png")
        
    def obtain_item(self, item, screen) :
        for i in range (9) :
                if self.item_status[i] == 0 :
                    self._set_Item(item)
                    self.item_status[i] = 1 
                    screen.blit(item._get_Picture(), (self.x + 373, self.y + 65))
        
 
    #def _obtain_item(self, item, screen, font) :
        #for i in range (9) :
                #if self.item_status[i] == 0 :
                    #self._set_Item(item)
                    #self.item_status[i] = 1 
                    #screen.blit(item._get_Picture(), (self.x + 373, self.y + 65))

        #if item == "epee_du_voyageur" :
            #self._set_inventory(item)
            #screen.blit(item._get_Picture(), (self.x + 373, self.y + 65))
            #screen.blit(font.render("Vous obtenez : ", item._get_Name(), True, (255, 255, 255)), (100, 500)) 
            

