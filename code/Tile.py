import pygame
import Object
import Enter

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.enters={}
        self.tile_map = surf

    def _add_enter(self, x, y name):
        self.enters[name]=x
        

    def _add_oject(x, y, object :object):

    def _add_Teleporter(x, y, teleporter :teleporter):