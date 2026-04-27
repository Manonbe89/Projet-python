import pygame
from Code.text_box import Text_Box
from Code.npc.npc import NPC


class Interaction:
    def __init__(self, player):
        self.player = player
        self.last_space_action = False
        self.in_action = False

    #fonction d'interaction avec les npc (affiche une bulle de dialogue quand le joueur appuie sur espace à proximité d'un npc)
    def _interact_npc(self, npc_group, screen, font):
        npc = self._search_npc(npc_group)
        if npc is None:
            return

        self._interact_with_text(screen, font, npc.text_box)



    #fonction qui cherche un npc à proximité du joueur (dans un rayon de 20 pixels)
    def _search_npc(self, npc_group):
        interaction_rect = self.player.hitbox.copy()
        interaction_rect.inflate_ip(20, 20)
        for npc in npc_group:
            if interaction_rect.colliderect(npc.hitbox):
                return npc
        return None
    
    #fonction d'interaction avec une bulle de dialogue (gère l'affichage du texte et la pagination)
    def _interact_with_text(self, screen, font, text_box):
        space_action = self.player.game.actions['space']
        space = space_action and not self.last_space_action

        if self.in_action:
            # gérer la pagination
            still_talking = self._handle_textbox(text_box, screen, font, space)

            if not still_talking:
                self.in_action = False

        else:
            # ouverture du texte
            if space:
                self.in_action = True
                text_box._reset()
                text_box._show_text(screen, font)

        self.last_space_action = space_action

    
    def _handle_textbox(self, text_box, screen, font, space):
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
        text_box._show_text(screen, font)
        return True

    
    #renvoie l'état d'interaction du joueur
    def _get_state(self):
        return self.in_action