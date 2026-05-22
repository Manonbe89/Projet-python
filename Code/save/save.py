import pygame
import json

pygame.init()

class Save() :
    def __init__(self) :
        self.file = 0
        self.picture = pygame.image.load("C:/Users/manon/Documents/Projet python S4/Frames/Test menu jeu.png").convert_alpha()
        self.buttons = []
        self.status_buttons = [0]
        self.buttons.append(pygame.Rect(327, 359 , 250, 59))
        self.menu = 1


    def _get_data(self, inventory) :
        current_item = str(inventory._get_current_Item())
        nb_current_item = str(inventory._get_nb_current_Item())
        item_status = str(inventory._get_item_status())
        data = {"current_item": current_item,
                "nb_current_item": nb_current_item,
                "item_status": item_status,
                "file" : self.file
                }
        with open("Code/save/save.json", "w") as file :
            json.dump(data, file, indent=4)


    def _load_data(self, screen) :
        self._display_menu(screen)
            
        if self.file != 0 :
           with open("Code/save/save.json", "r") as file :
               data = json.load(file)
               print (data)
               self.file = 1
        
    def _check_buttons(self, event) :
        if not self.status_buttons[0] :
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buttons[0].collidepoint(event.pos) :
                    self.status_buttons[0] = 1

    def _display_menu(self, screen) :
        if not self.status_buttons[0] :
            screen.blit(self.picture, (0, 0))
            pygame.display.flip()

    def _get_state_menu(self) :
        return self.status_buttons[0]

