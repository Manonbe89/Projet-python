import pygame
import sys
from Code.item.item import Item

pygame.init()   #initialisation de pygame


class Usable_Item (Item):
    def __init__(self, id, name, usage, description, picture):
        self.id = id
        self.name = name
        self.usage = usage
        self.description = description
        self.picture = picture
        self.picture_load = pygame.image.load(picture).convert_alpha()
        self.use_item = False       #booléen qui verifie si on a utilise un item
        self.dialogue_step = 0


    def _check_item_status_(self, event):
         if event.type == pygame.KEYDOWN :           # vérifie si l'événement keydown s'est produit ou non
              if event.key == pygame.K_u :           # vérifie si la touche "u" a été pressée
                   self.dialogue_step += 1
                   self.use_item = False


    def _Use_Item_(self, player, screen, font, inventory):
            item = inventory._get_consumable_Item()
            if self.dialogue_step == 1 :
                screen.blit(font.render("Vous utilisez : " + item._get_Name(), True, (255, 255, 255)), (300, 200))  #affiche le texte
                self._show_passage_text(1, screen, font)

            elif self.dialogue_step == 2 :
                            
                            if item._get_Name() == "potion" :
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                                  self._show_passage_text(1, screen, font) 
                                  if self.use_item == False : 
                                      self.use_item = True
                                    
                                  
                            if item._get_Name() == "bracelet de force" :
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                                self._show_passage_text(1, screen, font) 
                                if self.use_item == False : 
                                      self.use_item = True

                            if item._get_Name() == "bombe" :
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                                self._show_passage_text(1, screen, font) 
                                if self.use_item == False : 
                                      self.use_item = True

                            if item._get_Name() == "epee du voyageur" :
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                                screen.blit(item._get_Picture(), (300, 250))
                                self._show_passage_text(1, screen, font) 
                                if self.use_item == False : 
                                      player._set_stat("attack", 5)
                                      self.use_item = True

                            if item._get_Name() == "vieux grimoire" : 
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                self._show_passage_text(1, screen, font)
                                screen.blit(item._get_Picture(), (300, 250))
                                if self.use_item == False : 
                                      player._set_stat("magic", 5)
                                      self.use_item = True  

                            if item._get_Name() == "cuirasse" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  self._show_passage_text(1, screen, font)
                                  if self.use_item == False : 
                                      player._set_stat("armor", 5)
                                      self.use_item = True  
                                   
                            if item._get_Name() == "chapeau de magicien" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  self._show_passage_text(1, screen, font)
                                  if self.use_item == False : 
                                      player._set_stat("magic armor", 5)
                                      self.use_item = True 

                            if item._get_Name() == "chaussures en cuir" : 
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                self._show_passage_text(1, screen, font)
                                if self.use_item == False : 
                                      player._set_stat("armor", 2)
                                      player._set_stat("speed", 3)
                                      self.use_item = True  

                            if item._get_Name() == "masse nain" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  if self.use_item == False : 
                                      player._set_stat("attack", 10)
                                      player._set_stat("speed", -5)
                                      self.use_item = True 

                            if item._get_Name() == "plastron d'armure" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  if self.use_item == False : 
                                      player._set_stat("armor", 10)
                                      player._set_stat("magic armor", -5)
                                      self.use_item = True 

                            if item._get_Name() == "soleret" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  if self.use_item == False : 
                                      player._set_stat("armor", 10)
                                      player._set_stat("speed", -5)
                                      self.use_item = True 

            elif self.dialogue_step >= 3 :
                             self.dialogue_step = 0


    def _show_passage_text(self, number, screen, font):
         if number == 1 :
              screen.blit(font.render("Appuyer sur 'u' pour continuer", True, (255, 255, 255)), (100, 500))  
            