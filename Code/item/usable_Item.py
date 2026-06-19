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
        self.font = pygame.font.Font(None, 32)


    def _use_usable_Item(self, player, screen, inventory, item):
            if item._get_Name() != "" :
                if inventory._get_state() == False :
                    if item.dialogue_step == 1 :
                        screen.blit(self.font.render("Vous utilisez : " + item._get_Name(), True, (255, 255, 255)), (300, 200))  #affiche le texte
                        self._show_passage_text(1, screen, self.font)

                    elif item.dialogue_step == 2 :
                        screen.blit(self.font.render(item._get_Usage(), True, (255, 255, 255)), (300, 200))
                        item._show_passage_text(1, screen, self.font) 
                        self._apply_effect(item, player)
                                     
                    elif item.dialogue_step >= 3 :
                        item.dialogue_step = 0
                        item.use_item = False
                    
            else :
                 screen.blit(self.font.render("Désolé, vous n'avez rien en main", True, (255, 255, 255)), (100, 500))  
        
    def _apply_effect(self, item, player) :

        if item.use_item == False : 
                
                if item._get_Name() == "bracelet de force" :
                     player._set_stat("attack", 5)
                     item.use_item = True

                if item._get_Name() == "epee du voyageur" :
                    player._set_stat("attack", 5)
                    item.use_item = True

                if item._get_Name() == "vieux grimoire" : 
                    player._set_stat("magic", 5)
                    item.use_item = True  

                if item._get_Name() == "cuirasse" : 
                    player._set_stat("armor", 5)
                    item.use_item = True
                                   
                if item._get_Name() == "chapeau de magicien" :
                    player._set_stat("magic armor", 5)
                    item.use_item = True

                if item._get_Name() == "chaussures en cuir" :
                    player._set_stat("armor", 2)
                    player._set_stat("speed", 3)
                    item.use_item = True 

                if item._get_Name() == "masse nain" : 
                    player._set_stat("attack", 10)
                    player._set_stat("speed", -5)
                    item.use_item = True 

                if item._get_Name() == "plastron d'armure" : 
                    player._set_stat("armor", 10)
                    player._set_stat("magic armor", -5)
                    item.use_item = True

                if item._get_Name() == "soleret" : 
                    player._set_stat("armor", 10)
                    player._set_stat("speed", -5)
                    item.use_item = True

                if item._get_Name() == "bottes de pegase" : 
                     player._set_stat("armor", -5)
                     player._set_stat("magic armor", -5)
                     player._set_stat("speed", 15)

                if item._get_Name() == "arc elfique" : 
                     player._set_stat("attack", 5)
                     player._set_stat("armor", -3)
                     player._set_stat("magic armor", -2)
                     player._set_stat("speed", 5)

                if item._get_Name() == "tenue de garde elfique" : 
                     player._set_stat("armor", 5)
                     player._set_stat("magic armor", -5)
                     player._set_stat("speed", 5)         

                if item._get_Name() == "tenue de sage elfique" : 
                     player._set_stat("armor", -5)
                     player._set_stat("magic", 5)
                     player._set_stat("magic armor", 5)       

                if item._get_Name() == "grand sceptre" : 
                     player._set_stat("attack", -5)
                     player._set_stat("magic", 10)