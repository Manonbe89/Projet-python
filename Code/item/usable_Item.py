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


    def _Use_Item(self, player, screen, font, inventory, item):
            
            if inventory._get_state() == False :
                if item.dialogue_step == 1 :
                    screen.blit(font.render("Vous utilisez : " + item._get_Name(), True, (255, 255, 255)), (300, 200))  #affiche le texte
                    self._show_passage_text(1, screen, font)

                elif item.dialogue_step == 2 :
                            
                            if item._get_Name() == "potion" :
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                                  self._show_passage_text(1, screen, font) 
                                  if item.use_item == False : 
                                      item.use_item = True
                                    
                                  
                            if item._get_Name() == "bracelet de force" :
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                                self._show_passage_text(1, screen, font) 
                                if item.use_item == False : 
                                      item.use_item = True

                            if item._get_Name() == "bombe" :
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                                self._show_passage_text(1, screen, font) 
                                if item.use_item == False : 
                                      item.use_item = True

                            if item._get_Name() == "epee du voyageur" :
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                                screen.blit(item._get_Picture(), (300, 250))
                                self._show_passage_text(1, screen, font) 
                                if item.use_item == False : 
                                      player._set_stat("attack", 5)
                                      item.use_item = True

                            if item._get_Name() == "vieux grimoire" : 
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                self._show_passage_text(1, screen, font)
                                screen.blit(item._get_Picture(), (300, 250))
                                if item.use_item == False : 
                                      player._set_stat("magic", 5)
                                      item.use_item = True  

                            if item._get_Name() == "cuirasse" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  self._show_passage_text(1, screen, font)
                                  if item.use_item == False : 
                                      player._set_stat("armor", 5)
                                      item.use_item = True
                                   
                            if item._get_Name() == "chapeau de magicien" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  self._show_passage_text(1, screen, font)
                                  if item.use_item == False : 
                                      player._set_stat("magic armor", 5)
                                      item.use_item = True

                            if item._get_Name() == "chaussures en cuir" : 
                                screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                self._show_passage_text(1, screen, font)
                                if item.use_item == False : 
                                      player._set_stat("armor", 2)
                                      player._set_stat("speed", 3)
                                      item.use_item = True 

                            if item._get_Name() == "masse nain" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  if item.use_item == False : 
                                      player._set_stat("attack", 10)
                                      player._set_stat("speed", -5)
                                      item.use_item = True 

                            if item._get_Name() == "plastron d'armure" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  if item.use_item == False : 
                                      player._set_stat("armor", 10)
                                      player._set_stat("magic armor", -5)
                                      item.use_item = True

                            if item._get_Name() == "soleret" : 
                                  screen.blit(font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200)) 
                                  if item.use_item == False : 
                                      player._set_stat("armor", 10)
                                      player._set_stat("speed", -5)
                                      item.use_item = True

                elif item.dialogue_step >= 3 :
                     item.dialogue_step = 0
                     item.use_item = False


    def _show_passage_text(self, number, screen, font):
         if number == 1 :
              screen.blit(font.render("Appuyer sur 'u' pour continuer", True, (255, 255, 255)), (100, 500))  
            