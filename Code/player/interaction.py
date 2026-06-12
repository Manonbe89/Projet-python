import pygame
from Code.text_box import Text_Box
from Code.npc.npc import NPC
from Code.fight.fight import Fight


class Interaction:
    def __init__(self, player):
        self.player = player
        self.last_space_action = False
        self.in_action = False
        self.state = 'world'
        self.current_enemy = None
        self.interaction_rect = self.player.hitbox.copy()
        self.interaction_rect.inflate_ip(20, 20)

    def _search_enemy(self, enemy_group):
        for enemy in enemy_group:
            if self.interaction_rect.colliderect(enemy._get_hitbox()):
                self.in_action = True
                self.state = 'fight'
                self.current_enemy = enemy
                return enemy
        return None

    def _intercat_with_enemy(self, enemy_group):
        enemy = self._search_enemy(enemy_group)
        if enemy is None:
            return

        entities = [self.player.fight_entity._clone(), self.player.fight_entity._clone(), enemy.fight_entity._clone(), enemy.fight_entity._clone()]
        print ("here enemy")
        self._start_combat(entities,allies_nb=2)

    def _start_combat(self, entities, allies_nb):
        self.current_fight = Fight(entities, allies_nb)

    def _get_current_fight(self):
        return self.current_fight

    #fonction d'interaction avec les npc (affiche une bulle de dialogue quand le joueur appuie sur espace à proximité d'un npc)
    def _interact_npc(self, npc_group, screen):
        npc = self._search_npc(npc_group)
        if npc is None:
            return

        self._interact_with_text(screen, self.font, npc.text_box)



    #fonction qui cherche un npc à proximité du joueur (dans un rayon de 20 pixels)
    def _search_npc(self, npc_group):
        for npc in npc_group:
            if self.interaction_rect.colliderect(npc.hitbox):
                return npc
        return None
    
    #fonction d'interaction avec une bulle de dialogue (gère l'affichage du texte et la pagination)
    def _interact_with_text(self, screen, text_box):
        space_action = self.player.action.actions['space']
        space = space_action and not self.last_space_action

        if self.in_action:
            # gérer la pagination
            still_talking = self._handle_textbox(text_box, screen, self.font, space)

            if not still_talking:
                self.in_action = False

        else:
            # ouverture du texte
            if space:
                self.in_action = True
                text_box._reset()
                text_box._show_text(screen, self.font)

        self.last_space_action = space_action

    
    def _handle_textbox(self, text_box, screen, space):
        # si on vient d'appuyer sur espace
        if space:
            # s'il reste une page → page suivante
            if text_box._has_next_page():
                text_box._next_page()
            else:
                # plus de pages → fin du dialogue
                text_box._reset()
                return False

        # afficher la page courante
        text_box._show_text(screen, self.font)
        return True

    
    #renvoie l'état d'interaction du joueur
    def _get_state(self):
        return self.in_action
    
    def _get_world_state(self):
        return self.state
    
    def _set_world_state(self, world_state):
        self.state = world_state

    def _return_to_world(self):
        self.state = 'world'
        self.in_action = False

    def _update_interaction_rect(self):
        self.interaction_rect = self.player.hitbox.copy()
        self.interaction_rect.inflate_ip(20, 20)

    def _interact(self,enemy_group, npc_group, screen):
        self._update_interaction_rect()
        self._interact_npc(npc_group, screen)
        self._intercat_with_enemy(enemy_group)