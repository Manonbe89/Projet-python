import pygame
from Code.fight.fight_menu import Fight_Menu
from Code.fight.fight_calculator import Fight_calculator
from Code.fight.fight_action import Fight_action
import random

class Fight : 

    def __init__(self, entities, allies_nb):
        self.entities = entities
        self.background_image = pygame.image.load('Images/fond gris.png').convert_alpha()
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
        self.hp_font = pygame.font.Font(None, 24)
        self.win = False

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

        if not self.menus:
            return

        for i, ally in enumerate(self.allies):
            pos = (100, 50 + 150 * i )
            screen.blit(ally._get_sprite(), pos)
            self._draw_hp(screen, ally, pos)

        menu = self.menus[self.active_menu_index]

        for i, enemy in enumerate(self.enemys):
            pos = (800,100*(i+1))
            sprite = enemy._get_sprite()

            screen.blit(sprite, pos)
            self._draw_hp(screen, enemy, pos)

            if menu.selecting_target and i == self.target_index:
                rect = sprite.get_rect(topleft=pos)
                pygame.draw.rect(
                    screen,
                    (255,255,0),
                    rect.inflate(10,10),
                    3
                )

        self.menus[self.active_menu_index]._draw(screen)

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
            if enemy.is_dead():
                continue
            actions.append(Fight_action(enemy, "Attaque physique", random.choice(self.allies)))
        return actions
    
    def _get_all_actions(self):
        actions = []

        for menu in self.menus:
            if menu.locked_action is not None:
                if not menu.locked_action.user.is_dead():
                    actions.append(menu.locked_action)

        actions += self._get_enemy_actions()

        actions.sort(key=lambda action: action.user._get_stat("speed"), reverse=True)
        return actions

    def _resolve_turn(self):
        actions = self._get_all_actions()
        for action in actions:
            if not action._get_user().is_dead():
                self.finished = self.fight_calculator._execute_action(action, self.enemys, self.allies)
                self._remove_dead_entities()
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
    
    def _draw_hp(self, screen, entity, pos):
        sprite = entity._get_sprite()

        current_hp = entity._get_stat("life")
        max_hp = entity._get_max_life()

        hp_text = self.hp_font.render(
            f"{current_hp:.0f}/{max_hp:.0f}",
            True,
            (255, 255, 255)
        )

        text_rect = hp_text.get_rect(
            center=(
                pos[0] + sprite.get_width() // 2,
                pos[1] + sprite.get_height() + 15
            )
        )

        screen.blit(hp_text, text_rect)

    def _remove_dead_entities(self):
        self.allies = [a for a in self.allies if not a.is_dead()]
        self.enemys = [e for e in self.enemys if not e.is_dead()]
        self.menus = [m for m in self.menus if not m.entity.is_dead()]
        
        if not self.allies:
            self.win = False
            self.finished = True
            return

        if not self.enemys:
            self.win = True
            self.finished = True
            return

    def _is_win(self):
        return self.win
        