import pygame
import Wall

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)
        self.enters = {}
        self.objects = {}
        self.teleporters = {}
        self.tile_map = surf
        self.screen = pygame.display.set_mode((1000, 500))

    def _add_enter(self, x, y, name):
        self.enters[name] = (x, y)

    def _add_object(self, name, obj, x, y):
        obj.rect.topleft = (x, y)
        self.objects[name] = obj

    def _add_teleporter(self, name, teleporter, x, y):
        teleporter.rect.topleft = (x, y)
        self.teleporters[name] = teleporter

    def _charge(self):
        # Affiche la map
        self.screen.blit(self.tile_map, (0, 0))

        # Affiche chaque objet
        for obj in self.objects.values():
            self.screen.blit(obj.image, obj.rect)