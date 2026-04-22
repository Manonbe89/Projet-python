class Interaction:
    def __init__(self, player):
        self.player = player
        self.last_space_action = False
        self.in_action = False

    def _interact_npc(self, npc_group, screen, font):
        space_action = self.player.game.actions['space']
        space = space_action and not self.last_space_action
        
        npc = self._search_npc(npc_group)
        
        if self.in_action :
            if space :
                self.in_action = False

            else :
                if npc is not None:
                    npc._show_quote(screen, font)

        else :
            if npc is not None and space:
                self.in_action = True
                npc._show_quote(screen, font)

        self.last_space_action = space_action

    def _search_npc(self, npc_group):
        interaction_rect = self.player.hitbox.copy()
        interaction_rect.inflate_ip(20, 20)
        for npc in npc_group:
            if interaction_rect.colliderect(npc.hitbox):
                return npc
        return None