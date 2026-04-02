import pygame
import Wall

#"Tuile" de map (grand bout de carte)
class Tile:

    #constituer d'une surface et de liste d'obstacle d'entrer et de téleporteur
    def __init__(self, surf, collision_sprites):
        self.enters = {}
        self.objects = {}
        self.teleporters = {}
        self.tile_map = surf
        self.collision_sprites = collision_sprites

    #ajoute une entré à la tuile (une entré permet de savoir où le joueur doit apparaitre au chargements de la tuile)
    def _add_enter(self, x, y, name):
        self.enters[name] = (x, y)

    #ajoute un obstacle à la tuile
    def _add_object(self, name, x, y, surf):
        wall = Wall((x, y), surf, self.collision_sprites)
        key = f"{name}_{x}_{y}"         #création d'un clé unique à partir du nom de l'obstacle et de ces coordonées
        self.objects[key] = wall

    #ajoute un téleporteur à la tuile (un téleporteur permet )
    def _add_teleporter(self, name, teleporter, x, y):
        teleporter.rect.topleft = (x, y)
        self.teleporters[name] = teleporter

    #charge la map et les différents élements qui lui sont associé
    def _draw(self, screen):
        screen.blit(self.tile_map, (0, 0))
        for obj in self.objects.values():
            screen.blit(obj.image, obj.rect)