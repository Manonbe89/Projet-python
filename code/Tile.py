import pygame
import Wall

class Tile:
    def __init__(self, surf, collision_sprites):
        self.enters = {}
        self.objects = {}
        self.teleporters = {}
        self.tile_map = surf
        self.collision_sprites = collision_sprites

    def _add_enter(self, x, y, name):
        self.enters[name] = (x, y)

    def _add_object(self, name, x, y, surf):
        wall = Wall((x, y), surf, self.collision_sprites)
        key = f"{name}_{x}_{y}"
        self.objects[key] = wall

    def _add_teleporter(self, name, teleporter, x, y):
        teleporter.rect.topleft = (x, y)
        self.teleporters[name] = teleporter

    def _draw(self, screen):
        screen.blit(self.tile_map, (0, 0))
        for obj in self.objects.values():
            screen.blit(obj.image, obj.rect)