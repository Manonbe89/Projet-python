class Interaction:
    def __init__(self, player):
        self.player = player
        self.last_space_action = False
        self.in_action = False

    #fonction d'interaction avec les npc (affiche une bulle de dialogue quand le joueur appuie sur espace à proximité d'un npc)
    def _interact_npc(self, npc_group, screen, font):
        #cherche si le joueur apuye sur la touche espace
        space_action = self.player.game.actions['space']

        #cherche si le joueur vient juste d'appuyer sur la touche espace (pour éviter que l'action se répète tant que la touche est maintenue)
        space = space_action and not self.last_space_action
        
        #cherche si un npc est à proximité du joueur
        npc = self._search_npc(npc_group)
        
        #regarde si le joueur est déjà en train d'interagir avec un npc
        if self.in_action :

            #ferme le dialogue si le joueur appuie à nouveau sur espace
            if space :
                self.in_action = False

            #sinon réaffiche le dialogue du npc
            else :
                if npc is not None:
                    npc._show_quote(screen, font)

        #si le joueur n'est pas déjà en train d'interagir avec un npc, regarde si il y en a un à proximité
        else :
            #si il y en a un et que le joueur appuie sur espace, affiche le dialogue du npc
            if npc is not None and space:
                self.in_action = True           #variable qui empecheras le joueur de bouger ou de faire d'autre action
                npc._show_quote(screen, font)

        self.last_space_action = space_action   #sauvegarde le dernier espace

    #fonction qui cherche un npc à proximité du joueur (dans un rayon de 20 pixels)
    def _search_npc(self, npc_group):
        interaction_rect = self.player.hitbox.copy()
        interaction_rect.inflate_ip(20, 20)
        for npc in npc_group:
            if interaction_rect.colliderect(npc.hitbox):
                return npc
        return None
    
    #renvoie l'état d'interaction du joueur
    def _get_state(self):
        return self.in_action