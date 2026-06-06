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

        self.target_index = 0
        self.selecting_target = True
        self.finished = False

    def _handle_event(self, event):

        if self.state != "INPUT":
            return

        menu = self.menus[self.active_menu_index]

        if menu.selecting_target:
            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_DOWN:
                    self.target_index = (self.target_index - 1) % len(self.enemys)

                elif event.key == pygame.K_UP:
                    self.target_index = (self.target_index + 1) % len(self.enemys)

                elif event.key == pygame.K_SPACE:
                    menu.target = self.enemys[self.target_index]
                    menu.finished = True
                    menu.selecting_target = False
                    self._lock_action()

                elif event.key == pygame.K_ESCAPE:
                    menu.selecting_target = False
            return

        menu._handle_event(event)

        if (menu.finished and menu._get_selected_option() in ("Objet", "Fuir")):
            self._lock_action()

    def _draw(self, screen):
        screen.blit(self.background_image, (0,0))
        for i, ally in enumerate(self.allies):
            screen.blit(ally._get_sprite(), (100,100*(i+1)))

        menu = self.menus[self.active_menu_index]

        for i, enemy in enumerate(self.enemys):
            pos = (800,100*(i+1))
            sprite = enemy._get_sprite()

            screen.blit(sprite, pos)

            if menu.selecting_target and i == self.target_index:
                rect = sprite.get_rect(topleft=pos)
                pygame.draw.rect(
                    screen,
                    (255,255,0),
                    rect.inflate(10,10),
                    3
                )

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

    def _resolve_turn(self):
        actions = self._get_all_actions()
        for action in actions:
            self.finished = self.fight_calculator._execute_action(action, self.enemys, self.allies)
            if self.finished == True:
                return

        self.state = "INPUT"
        for menu in self.menus:
            menu._reset()

    def _lock_action(self):
        menu = self.menus[self.active_menu_index]

        if menu._get_selected_option() in ("Objet", "Fuir"):
            menu.target = menu._get_entity()

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

    def _is_finished(self):
        return self.finished

    
        