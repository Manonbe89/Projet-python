import pygame
import Wall

class Tile(pygame.sprite.Sprite):
    def __init__(self, groups, surf):
        super().__init__(groups)

        self.enters = {}
        self.objects = {}
        self.teleporters = {}
        self.tile_map = surf

    def _add_enter(self, x, y, name):
        self.enters[name] = (x, y)

    def _add_object(self, name, x, y, surf):
        #Création du mur
        wall = Wall.Wall((x, y), surf, self.collision_sprites)

        #Création d’un nom unique basé sur le nom + coordonnées
        key = f"{name}_{x}_{y}"

        #Stockage dans les objets
        self.objects[key] = wall

    def _add_teleporter(self, name, teleporter, x, y):
        teleporter.rect.topleft = (x, y)
        self.teleporters[name] = teleporter

    def _draw(self, screen):
        # Affiche la map
        screen.blit(self.tile_map, (0, 0))

        # Affiche chaque objet
        for obj in self.objects.values():
            self.screen.blit(obj.image, obj.rect)