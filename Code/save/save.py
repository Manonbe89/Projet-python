import pygame
import json
import os

pygame.init()

class Save() :
    def __init__(self) :
        self.picture = pygame.image.load("Images/Test_menu_jeu.png").convert_alpha()
        self.menu = 1
        self.buttons = []
        self.status_buttons = [0]
        self.buttons.append(pygame.Rect(327, 196 , 250, 59))
        self.buttons.append(pygame.Rect(327, 359 , 250, 59))


    def _get_data(self, inventory, player, map) :
        if self.status_buttons[0] : 
            nb_current_item = inventory._get_nb_current_Item()
            item_status = inventory._get_item_status()
            stats_player = player._get_stat_table() 
            player_position = {"x" : player._get_pos(0), "y" :player._get_pos(1)}  
            player_money = player._get_Money() 
            current_map = map._get_name_current_map()
            data = {"inventory" : {"nb_current_item": nb_current_item,
                                   "item_status": item_status},
                    "player" : {"stats_player" : stats_player,
                                "player_position" : player_position,
                                 "money" : player_money
                                 },
                    "map" : {"current_map" : current_map}
                                   }
            with open("Code/save/save.json", "w") as file :
                json.dump(data, file, indent=4)
            print("Sauvegarde effectuée")
            self.status_buttons[0] = 0


    def _load_data(self, screen, inventory, player, map) :
        self._display_menu(screen)
        fileName = "Code/save/save.json"
        if os.path.isfile(fileName) and os.path.getsize(fileName) != 0 :    #verifie que le fichier existe et qu'il n'est pas vide
            with open(fileName, "r") as file :
                data = json.load(file)
                inventory._set_nb_current_Item(int(data["inventory"]["nb_current_item"]))
                inventory._set_item_status(list(data["inventory"]["item_status"]))
                player._set_stat_table(data["player"]["stats_player"])
                player._set_pos(data["player"]["player_position"]["x"], data["player"]["player_position"]["y"])
                player._set_Money(data["player"]["player_money"])
                map._set_current_map(data["map"]["current_map"])

        
    def _check_buttons(self, event) :
        if self.menu :
            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.buttons[0].collidepoint(event.pos) :
                    self.status_buttons[0] = 1
                elif self.buttons[1].collidepoint(event.pos) :
                    self.menu = 0

        elif event.type == pygame.KEYDOWN :
            if event.key == pygame.K_m :
                self.menu = 1

    def _display_menu(self, screen) :
        if self.menu :
            screen.blit(self.picture, (0, 0))
            pygame.display.flip()

    def _get_state_menu(self) :
        return self.menu

