import pygame
from Code.map.wall import Wall
from Code.npc.npc import NPC
from Code.map.collision_group import Collision_groups

#"Tuile" de map (grand bout de carte)
class Tile:

    #constituer d'une surface et de liste d'obstacle d'entrer et de téleporteur
    def __init__(self, surf):
        self.enters = {}
        self.objects = {}
        self.teleporters = {}
        self.enemies = {}
        self.tile_map = surf
        self.solid_walls = pygame.sprite.Group()
        self.brekable_walls = pygame.sprite.Group()
        self.pushable_walls = pygame.sprite.Group()
        self.npc_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.collision_group = Collision_groups(self.solid_walls, self.pushable_walls, self.brekable_walls, self.npc_group)

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

    def _add_npc(self, name, surf, x, y, quote):
        npc = NPC(name, surf, (x, y), quote, self.npc_group)
        key = f"npc_{name}_{x}_{y}"
        self.objects[key] = npc

    def _add_ennemy(self, enemy_to_create, x, y):
        enemy = enemy_to_create._create_enemy((x, y), self.enemy_group, self)
        key = f"enemy_{enemy.name}_{x}_{y}"
        self.enemies[key] = enemy

    def _get_collision_groups(self):
        return self.collision_group

    #charge la map et les différents élements qui lui sont associé en prenant en compte la camera
    def _draw(self, screen, camera, dt, player, state):
        screen.blit(self.tile_map, (-camera.position.x, -camera.position.y))
        for obj in self.objects.values():
            screen.blit(obj.image, camera._apply(obj.rect))
        for enemy in self.enemies.values():
            enemy.update(dt, state, player)
            screen.blit(enemy.image, camera._apply(enemy.rect))

    def _delete_an_enemy(self, interaction):
        enemy = interaction.current_enemy
        if enemy is None:
            return

        enemy.kill()
        for key, value in list(self.enemies.items()):
            if value == enemy:
                del self.enemies[key]
                break
