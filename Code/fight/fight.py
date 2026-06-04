import pygame
from Code.fight.fight_menu import Fight_Menu
from Code.fight.fight_calculator import Fight_calculator
from Code.fight.fight_action import Fight_action
import random

class Fight : 

    def __init__(self, entities, allies_nb):
        self.entities = entities
        self.background_image = pygame.image.load('Images/fight_background.jpg').convert_alpha()
        self.allies = entities[:allies_nb]
        self.enemys = entities[allies_nb:]
        self.menus = []
        self.fight_calculator = Fight_calculator()
        self.active_menu_index = 0
        self.state = "INPUT"
        for ally in self.allies:
            self.menus.append(Fight_Menu(ally))


    def _handle_event(self, event):
        if self.state != "INPUT":
            return
        
        self.menus[self.active_menu_index]._handle_event(event)
        if self.menus[self.active_menu_index].finished:
            self._lock_action()

    def _draw(self, screen):
        screen.blit(self.background_image, (0,0))
        for i, ally in enumerate(self.allies):
            screen.blit(ally._get_sprite(), (100*(i+1),100*(i+1)))

        for i, enemy in enumerate(self.enemys):
            screen.blit(enemy._get_sprite(), (800*(i+1),100*(i+1)))

        for menu in self.menus:
            menu._draw(screen)

    def _update_turn(self):
        menu = self.menus[self.active_menu_index]
        if menu.finished:
            self._select_enemy(menu)
            self.active_menu_index += 1

            if self.active_menu_index >= len(self.menus):
                self.active_menu_index = 0
                self._resolve_turn()

    def _get_enemy_actions(self):
        actions = []
        for enemy in self.enemys:
            actions.append(Fight_action(enemy, "Attaque physique", random.choice(self.allies)))
        return actions
    
    def _get_all_actions(self):
        actions = []

        for menu in self.menus:
            if menu.locked_action is not None:
                actions.append(menu.locked_action)

        actions += self._get_enemy_actions()

        actions.sort(key=lambda action: action.user._get_stat("speed"), reverse=True)
        return actions
    
    def _select_enemy(self):
        menu = self.menus[self.active_menu_index]
        if menu._get_selected_option() in ("Objet","Fuir"):
            menu.target = menu._get_entity()

        else :
            menu.target = random.choice(self.enemys)

    def _resolve_turn(self):
        actions = self._get_all_actions()
        for action in actions:
            print(action.user.name, action.action_type, action.target.name)

        self.state = "INPUT"
        for menu in self.menus:
            menu._reset()

    def _lock_action(self):
        self._select_enemy()
        menu = self.menus[self.active_menu_index]

        menu.locked_action = Fight_action(
            menu._get_entity(),
            menu._get_selected_option(),
            menu._get_target()
        )
        self.active_menu_index += 1
        
        if self.active_menu_index >= len(self.menus):
            self.active_menu_index = 0
            self.state = "RESOLVE"
            self._resolve_turn()
    
        