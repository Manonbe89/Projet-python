import pygame
import Object

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.enters={}
        self.objects={}
        self.teleporters={}
        self.tile_map = surf
        self.screen = pygame.display.set_mode((1000,500))

    def _add_enter(self, x, y, name):
        self.enters[name]=(x, y)

    def _add_object(self, x, y, object :object):
        self.objects[object]=(x,y)

    def _add_Teleporter(self, x, y, teleporter :teleporter):
        self.teleporters=[teleporter]=(x,y)

    def _charge(self):
        screen.blit.