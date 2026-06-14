import pygame
from Code.map.map import Map

class Teleportation : 
    def __init__(self) :
        self.font = pygame.font.Font(None, 32)

    def _teleportation(self, player, map, screen) :
        if map._get_name_current_map() == 'bedroom' :
            if 396 < player._get_pos(0) < 509 and player._get_pos(1) == 510 :
                map._set_current_map('first_village')
                player._set_pos(490, 500)  
                self._chargement(screen)
                

        if map._get_name_current_map() == 'first_village' :
            if 495 <= player._get_pos(0) <= 510 and player._get_pos(1) == 470 :
                map._set_current_map('bedroom')
                player._set_pos(450, 480)
                self._chargement(screen)

            elif player._get_pos(0) == 500 and player._get_pos(1) >= -15 :
                map._set_current_map('intersection')
                player._set_pos(500, 980)
                self._chargement(screen)


        if map._get_name_current_map() == 'intersection' :
            if  0 <= player._get_pos(0) <= 33 and 430 <= player._get_pos(1) <= 570 :
                map._set_current_map('left_path')
                player._set_pos(962, 755)
                self._chargement(screen)
                

    def _chargement(self, screen) : 
        screen.fill((0, 0, 0))
        screen.blit(self.font.render("Chargement...", True, (255, 255, 255)), (100, 500)) 
        pygame.display.flip()
        pygame.time.delay(1000)


