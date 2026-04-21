import pygame
import sys
from item import Item

pygame.init()   #initialisation de pygame


class Usable_Item (Item):
    def __init__(self, id, name, picture, usage):
        self.id = id
        self.name = name
        self.picture = picture
        self.usage = usage
        self.use_item = False       #booléen qui verifie si on a utilise un item
        self.dialogue_step = 0


    def _get_Usage_(self):
        return self.usage


    def _check_item_status_(self, event):
         if event.type == pygame.KEYDOWN :           # vérifie si l'événement keydown s'est produit ou non
              if event.key == pygame.K_u :           # vérifie si la touche "u" a été pressée
                   self.dialogue_step += 1


    def _Use_Item_(self, player, uitem, screen, font):
            if self.dialogue_step == 1 :
                screen.blit(font.render("Vous utilisez : " + uitem._get_Name_(), True, (255, 255, 255)), (300, 200))  #affiche le texte
                uitem._show_passage_text(1, screen, font)

            elif self.dialogue_step == 2 :
                            if uitem._get_Name_() == "épée du voyageur" :
                                screen.blit(font.render("Vous gagnez 5 points d'attaque", True, (255, 255, 255)), (300, 200))
                                uitem._show_passage_text(1, screen, font) 
                                if self.use_item == False : 
                                      player._set_stat("attack", 5)
                                      self.use_item = True

                                if self.dialogue_step == 3 :
                                       screen.blit(font.render("Vos points d'attaque : " + str(player._get_stat("attack")), True, (255, 255, 255)), (300, 200)) 
                                       uitem._show_passage_text(1, screen, font)

                            if uitem._get_Name_() == "vieux grimoire" : 
                                screen.blit(font.render("Vous gagnez 5 points de magie", True, (255, 255, 255)), (300, 200)) 
                                uitem._show_passage_text(1, screen, font)
                                if self.use_item == False : 
                                      player._set_stat("magic", 5)
                                      self.use_item = True   

                                if self.dialogue_step == 3 :
                                       screen.blit(font.render("Vos points de magie : " + str(player._get_stat("attack")), True, (255, 255, 255)), (300, 200)) 
                                       uitem._show_passage_text(1, screen, font)

            elif self.dialogue_step >= 4 :
                             self.dialogue_step = 0


    def _show_passage_text(self, number, screen, font):
         if number == 1 :
              screen.blit(font.render("Appuyer sur 'u' pour continuer", True, (255, 255, 255)), (100, 550))  
              
