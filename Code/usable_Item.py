import pygame
import sys
from Code.item import Item

pygame.init()   #initialisation de pygame


class Usable_Item (Item):
    def __init__(self, id, name, picture, usage):
        self.id = id
        self.name = name
        self.picture = picture
        self.usage = usage
        self.use_item = False       #booléen qui verifie si on a utilise un item
        self.dialogue_step = 0
        #images
        self.image_epee = pygame.image.load("C:/Users/manon/Documents/Projet python S4/Frames/Objets/epee_2.png").convert_alpha()


    def _get_Usage_(self):
        return self.usage


    def _check_item_status_(self, event):
         if event.type == pygame.KEYDOWN :           # vérifie si l'événement keydown s'est produit ou non
              if event.key == pygame.K_u :           # vérifie si la touche "u" a été pressée
                   self.dialogue_step += 1
                   self.use_item = False


    def _Use_Item_(self, player, uitem, screen, font, inventory):
            uitem._set_Name_(inventory._get_current_item())
            if self.dialogue_step == 1 :
                screen.blit(font.render("Vous utilisez : " + uitem._get_Name_(), True, (255, 255, 255)), (300, 200))  #affiche le texte
                uitem._show_passage_text(1, screen, font)

            elif self.dialogue_step == 2 :
                            
                            if uitem._get_Name_() == "bracelet de force" :
                                screen.blit(font.render("A voir", True, (255, 255, 255)), (300, 200))
                                uitem._show_passage_text(1, screen, font) 
                                if self.use_item == False : 
                                      player._set_stat("attack", 5)
                                      self.use_item = True

                            if uitem._get_Name_() == "epee du voyageur" :
                                screen.blit(font.render("Vous gagnez 5 points d'attaque", True, (255, 255, 255)), (300, 200))
                                screen.blit(self.image_epee, (300, 250))
                                uitem._show_passage_text(1, screen, font) 
                                if self.use_item == False : 
                                      player._set_stat("attack", 5)
                                      self.use_item = True

                            if uitem._get_Name_() == "vieux grimoire" : 
                                screen.blit(font.render("Vous gagnez 5 points de magie", True, (255, 255, 255)), (300, 200)) 
                                uitem._show_passage_text(1, screen, font)
                                if self.use_item == False : 
                                      player._set_stat("magic", 5)
                                      self.use_item = True   

                            if uitem._get_Name_() == "chaussures en cuir" : 
                                screen.blit(font.render("Vous gagnez 2 points de defense et 3 points de vitesse", True, (255, 255, 255)), (300, 200)) 
                                uitem._show_passage_text(1, screen, font)
                                if self.use_item == False : 
                                      player._set_stat("armor", 2)
                                      player._set_stat("speed", 3)
                                      self.use_item = True  

            elif self.dialogue_step >= 3 :
                             self.dialogue_step = 0


    def _show_passage_text(self, number, screen, font):
         if number == 1 :
              screen.blit(font.render("Appuyer sur 'u' pour continuer", True, (255, 255, 255)), (100, 500))  
              
    def _set_Name_(self, new_name) :
          self.name = new_name
