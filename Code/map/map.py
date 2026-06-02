import pygame
from Code.map.camera import Camera
from Code.map.tile import Tile
from Code.map.object import Object


class Bedroom : 

    def __init__(self):
        self.name = 'bedroom'
        self.surf = pygame.image.load('Images/Chambre1.png').convert_alpha()
        self.camera = Camera(900, 600, 500, 500)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
    def _create_map(self):
        table = pygame.transform.scale(object.invisible_wall, (50,50))
        bed = pygame.transform.scale(object.invisible_wall, (50,50))
        top_bordure = pygame.transform.scale(object.invisible_wall, (1,500))
        side_bordure = pygame.transform.scale(object.invisible_wall, (500,1))
        self.tile._add_solid_walls('table', 250, 250, table)
        self.tile._add_solid_walls('bed', 250, 250, bed)
        self.tile._add_solid_walls('top_bordure', 0,0, top_bordure)
        self.tile._add_solid_walls('bot_bordure', 0,500, top_bordure)
        self.tile._add_solid_walls('left_bordure', 0,0, side_bordure)
        self.tile._add_solid_walls('right_bordure', 0,0, side_bordure)

    def _get_tile(self):
        return self.tile

class Map : 

    def __init__(self):
        self.bedroom = Bedroom()




        