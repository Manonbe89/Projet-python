import pygame
from Code.map.camera import Camera
from Code.map.tile import Tile
from Code.map.object import Object


class Bedroom : 

    def __init__(self):
        self.tile = Tile()
        self.object = Object()

    def _create_map():
        table = pygame.transform.scale(object.invisible_wall, (50,50))
        top_bordure = pygame.transform.scale(object.invisible_wall, (1,100))
        