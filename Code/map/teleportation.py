import pygame
from Code.map.map import Map

class Teleportation : 
    def __init__(self, map) :
        self.current_map = map._get_name_current_map()

    def _teleportation(self, player, map) :
        if self.current_map == 'bedroom' :
            if 396 < player._get_pos(0) < 509 and player._get_pos(1) == 510 :
                map._set_current_map('first_village')
                player._set_pos(490, 500)           
