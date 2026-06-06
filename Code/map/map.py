import pygame
from Code.map.camera import Camera
from Code.map.tile import Tile
from Code.map.object import Object


class Bedroom : 

    def __init__(self):
        self.name = 'bedroom'
        self.surf = pygame.image.load("Images/Chambre.png").convert_alpha()
        self.camera = Camera(900, 600, 500, 500)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self._create_map()

    def _create_map(self):
        table = pygame.transform.scale(self.object.invisible_wall, (130,135))
        bed = pygame.transform.scale(self.object.invisible_wall, (80,165))
        top_bordure = pygame.transform.scale(self.object.invisible_wall, (500,1))
        side_bordure = pygame.transform.scale(self.object.invisible_wall, (1,500))
        self.tile._add_solid_walls('table', 395, 235, table)
        self.tile._add_solid_walls('bed', 632, 60, bed)
        self.tile._add_solid_walls('top_bordure', 202,60, top_bordure)
        self.tile._add_solid_walls('bot_bordure', 202, 560, top_bordure)
        self.tile._add_solid_walls('left_bordure', 202,60, side_bordure)
        self.tile._add_solid_walls('right_bordure', 701,60, side_bordure)

    def _get_tile(self):
        return self.tile
    

class First_Village : 

    def __init__(self):
        self.name = 'first_village'
        self.surf = pygame.image.load("Images/Map.png").convert_alpha()
        self.camera = Camera(900, 600, 500, 500)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self._create_map()

    def _create_map(self):
        house = pygame.transform.scale(self.object.invisible_wall, (197,149))
        top_bordure = pygame.transform.scale(self.object.invisible_wall, (500,1))
        side_bordure = pygame.transform.scale(self.object.invisible_wall, (1,500))
        self.tile._add_solid_walls('table', 83, 97, house)
        self.tile._add_solid_walls('top_bordure', 30, 30, top_bordure)
        self.tile._add_solid_walls('bot_bordure', 30, 970, top_bordure)
        self.tile._add_solid_walls('left_bordure', 30, 30, side_bordure)
        self.tile._add_solid_walls('right_bordure', 970, 30, side_bordure)

    def _get_tile(self):
        return self.tile
    
class Map : 

    def __init__(self):
        self.bedroom = Bedroom()
        self.first_village = First_Village()
