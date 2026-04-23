import pygame
from Code.Map.wall import Wall

#"Tuile" de map (grand bout de carte)
class Tile:

    #constituer d'une surface et de liste d'obstacle d'entrer et de téleporteur
    def __init__(self, surf, solid_walls, breakable_walls, pushable_walls):
        self.enters = {}
        self.objects = {}
        self.teleporters = {}
        self.tile_map = surf
        self.solid_walls = solid_walls
        self.brekable_walls = breakable_walls
        self.pushable_walls = pushable_walls

    #ajoute une entré à la tuile (une entré permet de savoir où le joueur doit apparaitre au chargements de la tuile)
    def _add_enter(self, x, y, name):
        self.enters[name] = (x, y)

    #ajoute un obstacle solide à la tuile
    def _add_solid_walls(self, name, x, y, surf):
        wall = Wall((x, y), surf, self.solid_walls)
        key = f"solid_{name}_{x}_{y}"    #création d'un clé unique à partir du nom de l'obstacle et de ces coordonées
        self.objects[key] = wall

    #idem mais dans un autre groupe pour pouvoir gérer les murs cassables
    def _add_breakable_walls(self, name, x, y, surf):
        wall = Wall((x, y), surf, self.brekable_walls)
        key = f"breakable_{name}_{x}_{y}"
        self.objects[key] = wall

    #idem mais dans un autre groupe pour pouvoir gérer les murs poussables
    def _add_pushable_walls(self, name, x, y, surf):
        wall = Wall((x, y), surf, self.pushable_walls)
        key = f"pushable_{name}_{x}_{y}"
        self.objects[key] = wall   

    #ajoute un téleporteur à la tuile (un téleporteur permet d'aller sur une autre tuile)
    def _add_teleporter(self, name, teleporter, x, y):
        teleporter.rect.topleft = (x, y)
        self.teleporters[name] = teleporter

    #charge la map et les différents élements qui lui sont associé en prenant en compte la camera
    def _draw(self, screen, camera):
        screen.blit(self.tile_map, (-camera.position.x, -camera.position.y))
        for obj in self.objects.values():
            screen.blit(obj.image, camera.apply(obj.rect))
