#import Equipement
import pygame
import sys
from Code.item.item import Item

class Inventory:
    def __init__(self):
        self.item = [] 
        self.inventory = []
        self.item_status = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
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
    def _get_current_Item(self):
        if 0 <= self.current_item < len(self.item):
            return self.item[self.current_item]
    
    def _get_nb_current_Item(self) : 
        return self.current_item
    
    def _get_Item(self, index) :
        return self.item[index]
    
    def _get_item_status(self) : 
        return self.item_status
    
    def _get_state(self) :
        return self.open_inventory
    
#setters

    def _set_nb_current_Item(self, Item) : 
        self.current_item = Item

    def _set_Item(self, Item):
        self.item.append(Item)

    def _set_Inventory(self, Item) : 
        self.inventory.append(Item)

    def _set_item_status(self, index) :
        for i in range(len(self.item_status)) :
            if index[i] :
                self.item_status[i] = 1
            else :
                self.item_status[i] = 0


    def _check_inventory_status(self, event):
        if event.type == pygame.KEYDOWN :                           # vérifie si l'événement keydown s'est produit ou non
             if event.key == pygame.K_i :                           # vérifie si la touche "i" a été pressée
                self.open_inventory = not self.open_inventory       #inverse l'état de self.open_inventory

    def _display_inventory(self, screen, font):
        if self.open_inventory : 
            screen.blit(self.image, (self.x, self.y))                     #affiche l'écran d'inventaire

            if 0 <= self.current_item < len(self.item) and self.status_buttons[self.current_item] and self.item_status[self.current_item] :
                        item = self.item[self.current_item]
                        item._set_Name(item._get_Name())
                        screen.blit(item._get_Picture(), (self.x + 373, self.y + 65))
                        screen.blit(font.render(item._get_Description(), True, (0, 0, 0)), (self.x + 10, self.y + 330))

    def _check_buttons(self, event) :
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range (18) :
                if self.buttons[i].collidepoint(event.pos) and self.item_status[i] :
                    self.status_buttons[i] = 1
                    self.current_item = i
        
    def _obtain_item(self, item, screen, font) :
        for i in range (18) :
            if item == self._get_Item(i) and self.item_status[i] == 0 :
                    self._set_Inventory(item)
                    screen.blit(font.render("Vous obtenez : " + item._get_Name(), True, (255, 255, 255)), (100, 500)) 
                    print ("vous obenez : " + item._get_Name())
                    self.item_status[i] = 1

    def _display_item(self, screen) :
        if self.open_inventory : 
                
                item = self.item[self.current_item]

                if self.item_status[0] == 1 :
                    screen.blit(item._get_Picture(), (self.x + 29, self.y + 65))

                if self.item_status[4] == 1 :
                    screen.blit(item._get_Picture(), (self.x + 26, self.y + 171))

                if self.item_status[5] == 1 :
                    screen.blit(item._get_Picture(), (self.x + 89, self.y + 171))

                if self.item_status[6] == 1 :
                    screen.blit(item._get_Picture(), (self.x + 154, self.y + 171))

                if self.item_status[7] == 1 :
                    screen.blit(item._get_Picture(), (self.x + 215, self.y + 171))

                if self.item_status[8] == 1 :
                    screen.blit(item._get_Picture(), (self.x + 279, self.y + 171))

                if self.item_status[9] == 1 :
                    screen.blit(item._get_Picture(), (self.x + 343, self.y + 171))
 
    def _item_factory(self) :
        rien = Item(0, "rien", "Vous ne faites rien", "", "")
        epee_du_voyageur = Item(1, "epee du voyageur", "Vous gagnez 5 points d'attaque", "L'épée parfaite pour commencer une aventure", "Images/epee_2.png")
        potion = Item(2, "potion", "A voir", "Ce breuvage augmente considerablement la (statistique) de son utilisateur", "Images/potion_2.png")
        bracelet_de_force = Item(3, "bracelet de force", "A voir", "Avec ça plus aucun rocher ne vous résistera", "Images/bracelet de force_2.png")
        bombe = Item(4, "bombe", "A voir", "Attention à n'exploser personne", "Images/bombe_2.png")
        vieux_grimoire = Item(5, "vieux grimoire", "Vous gagnez 5 points de magie", "Le grimoire d'un magicien en herbe", "Images/Grimoire magique_2.png")
        cuirasse = Item(6, "cuirasse", "Vous gagnez 5 points de defense", "Une cuirasse robuste pour résister à n'importe quelle lame", "Images/cuirasse_2.png")
        chapeau_de_magicien = Item(7, "chapeau de magicien", "Vous gagnez 5 points de defense magique", "Ce chapeau aurait appartenu à un valeureux magicien, il vous protègera sûrement du mauvais sort", "Images/chapeau de magicien_2.png")
        chaussures_en_cuir = Item(8, "chaussures en cuir", "Vous gagnez 2 points de defense et 3 points de vitesse", "Elles vous ont été offertes par votre grand père, prenez en soin", "")
        masse_nain = Item(9, "masse nain", "Vous gagnez 10 points d'attaque et perdez 5 points de vitesse", "Une masse robuste maniée par les plus petits guerriers de ce monde", "")
        plastron_d_armure = Item(10, "plastron d'armure", "Vous gagnez 10 points de defense et perdez 5 points de defense magique", "Une armure capable d'arrêter n'importe quelle attaque, attention quand même aux sorts", "")
        soleret = Item(11, "soleret", "Vous gagnez 10 points de defense et perdez 5 points de vitesse", "Pour des pieds bien protégés", "")
        bottes_de_pegase = Item(12, "bottes de pegase", "Vous perdez 5 points de defense et de defense magique mais gagnez 15 points de vitesse", "Avec ces bottes vous serez sûr d'attaquer en premier, mais attention à la contre-attaque !", "")
        arc_elfique = Item(13, "arc elfique", "Vous gagnez 5 points d'attaque et de vitesse mais perdez 3 points de defense et 2 points de defense magique", "Pratique pour prendre un ennemi par surprise", "")
        tenue_de_garde_elfique = Item(14, "tenue de garde elfique", "Vous gagnez 5 points de defense et de vitesse mais perdez 5 points de defense magique", "Tenue traditionnelle des soldats elfes, elle s'adapte parfaitement à n'importe quel type de mouvement", "")
        tenue_de_sage_elfique = Item(15, "tenue de sage elfique", "Vous gagnez 5 points de magie et de defense magique mais perdez 5 points de defense", "L'ancienne tenue d'un noble elfe, elle convient à un mage expérimenté", "")
        grand_sceptre = Item(16, "grand sceptre", "Vous gagnez 10 points de magie mais perdez 5 points d'attaque", "Ce bâton légendaire aurait appartenu au célèbre gandolf le vert", "")
        self._set_Item(epee_du_voyageur)
        self._set_Item(rien)
        self._set_Item(rien)
        self._set_Item(rien)
        self._set_Item(potion)
        self._set_Item(bracelet_de_force)
        self._set_Item(bombe)
        self._set_Item(vieux_grimoire)
        self._set_Item(cuirasse)
        self._set_Item(chapeau_de_magicien)
        self._set_Item(chaussures_en_cuir)
        self._set_Item(masse_nain)
        self._set_Item(plastron_d_armure)
        self._set_Item(soleret)
        self._set_Item(bottes_de_pegase)
        self._set_Item(arc_elfique)
        self._set_Item(tenue_de_garde_elfique)
        self._set_Item(tenue_de_sage_elfique)
        self._set_Item(grand_sceptre)