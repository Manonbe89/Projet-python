import pygame

class Enemy_AI:
    def __init__(self):
        pass

    #chech if the player is in their detection range
    def _detect_player(self, player, enemy):
        detection_range = enemy._get_detection_range()
        if detection_range.colliderect(player.hitbox):
            return True
    
    #go in straight line at player position
    def _go_on_player_position(self, player, enemy):
        x_player = player._get_pos(0)
        y_player = player._get_pos(1)

        x_enemy = enemy._get_pos(0)
        y_enemy = enemy._get_pos(1)

        x_diference = x_player - x_enemy
        if x_diference < 0:
            enemy._set_direction(0, -1)
        elif x_diference > 0:
            enemy._set_direction(0, 1)
        elif x_diference == 0:
            enemy._set_directio,(0,0)

        y_diference = y_player - y_enemy
        if y_diference < 0:
            enemy._set_direction(1, -1)
        elif y_diference > 0:
            enemy._set_direction(1, 1)
        elif y_diference == 0:
            enemy._set_directio,(1,0)

    #do the AI calcul
    def _update(self, player, enemy):
        player_is_here = self._detect_player(player, enemy)
        if player_is_here:
            self._go_on_player_position(player, enemy)
        
