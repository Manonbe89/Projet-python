import pygame
from Code.map.map import Map

class Teleportation : 
    def __init__(self) :
        self.font = pygame.font.Font(None, 32)

    def _teleportation(self, player, map, screen, inventory) :
        if map._get_name_current_map() == 'bedroom' :
            if 396 < player._get_pos(0) < 509 and player._get_pos(1) == 510 :
                map._set_current_map('first_village')
                player._set_pos(490, 500)  
                self._chargement(screen)
                

        elif map._get_name_current_map() == 'first_village' :
            if 495 <= player._get_pos(0) <= 510 and player._get_pos(1) == 470 :
                map._set_current_map('bedroom')
                player._set_pos(450, 500)
                self._chargement(screen)

            elif player._get_pos(0) == 500 and 0 <= player._get_pos(1) <= 30 :
                map._set_current_map('intersection')
                player._set_pos(500, 920)
                self._chargement(screen)


        elif map._get_name_current_map() == 'intersection' :
            if 418 <= player._get_pos(0) <= 582 and 970 <= player._get_pos(1) <= 1000 :
                map._set_current_map('first_village')
                player._set_pos(500, 80)
                self._chargement(screen)
            
            elif 0 <= player._get_pos(0) <= 33 and 430 <= player._get_pos(1) <= 570 :
                map._set_current_map('left_path')
                player._set_pos(920, 755)
                self._chargement(screen)

            elif 970 <= player._get_pos(0) <= 1000 and 430 <= player._get_pos(1) <= 570 :
                map._set_current_map('right_path')
                player._set_pos(80, 755)
                self._chargement(screen)

            elif 418 <= player._get_pos(0) <= 582 and 0 <= player._get_pos(1) <= 30 :
                status = inventory._get_item_status()
                if status[3] == 1 and status[7] == 1 :
                    map._set_current_map('final_donjon')
                    player._set_pos(80, 755)
                    self._chargement(screen)
                else : 
                    self._check_item(screen)


        elif map._get_name_current_map() == 'left_path' :
            if 970 <= player._get_pos(0) <= 1000 and 673 <= player._get_pos(1) <= 838 :
                map._set_current_map('intersection')
                player._set_pos(80, 500)
                self._chargement(screen)

        elif map._get_name_current_map() == 'right_path' :
            if 0 <= player._get_pos(0) <= 30 and 673 <= player._get_pos(1) <= 838 :
                map._set_current_map('intersection')
                player._set_pos(920, 500)
                self._chargement(screen)

            if 685 <= player._get_pos(0) <= 849 and 0 <= player._get_pos(1) <= 30 :
                map._set_current_map('elf_village')
                player._set_pos(496, 900)
                self._chargement(screen)

                

    def _chargement(self, screen) : 
        screen.fill((0, 0, 0))
        screen.blit(self.font.render("Chargement...", True, (255, 255, 255)), (100, 500)) 
        pygame.display.flip()
        pygame.time.delay(1000)


    def _check_item(self, screen) :
        screen.blit(self.font.render("Vous n'avez pas les items requis", True, (255, 255, 255)), (100, 500)) 
        pygame.display.flip()
        pygame.time.delay(25)