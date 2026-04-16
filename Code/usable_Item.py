import pygame
import sys
from item import Item
from player import Player

pygame.init()   #initialisation de pygame

#initialisations pour le texte



class Usable_Item (Item):
    def __init__(self, id, name, picture, usage):
        self.id = id
        self.name = name
        self.picture = picture
        self.usage = usage

    def _get_Usage_(self):
        return self.usage

    def _Use_Item_(self, player, uitem, screen, font, event):
         
         if event.type == pygame.KEYDOWN :           # vérifie si l'événement keydown s'est produit ou non
              if event.key == pygame.K_u :           # vérifie si la touche "u" a été pressée
                screen.blit(font.render("Vous utilisez :" + uitem._get_Name_(), True, (255, 255, 255)), (300, 200))  #affiche le texte
                if (uitem._get_Name_() == "épée du voyageur"):
                    player._set_stat("attack", 5)
                    screen.blit(font.render("Vous gagnez 5 points d'attaque", True, (255, 255, 255)), (50, 50)) 