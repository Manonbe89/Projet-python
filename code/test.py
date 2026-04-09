import pygame

# FAUSSE CLASSE GAME

class FakeGame:
    def __init__(self):
        self.actions = {
            'move up': False,
            'move down': False,
            'move left': False,
            'move right': False
        }

class FakeTilesheet:
    def __init__(self, *args, **kwargs):
        pass

# CLASSE Collision_groups :

class Collision_groups : 
    # prend les différents groupe du super groupe en entré
    def __init__(self, *groups):
        self.groups = groups

    # copie les sprite des différents objet des différents groupe en evitant les doublons
    def _sprites(self):
        combined = set()
        for g in self.groups:
            combined.update(g.sprites())
        return list(combined)

    # permet l'itération (for x in Collision_groups)
    def __iter__(self):
        return iter(self.sprites())

    #permet d'utiliser la methode len(Collision_groups)
    def __len__(self):
        return len(self.sprites())

# CLASSE WALL

class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

        self.hitbox = self.rect.copy().inflate(
            -self.rect.width * 0,
            -self.rect.height * 0
        )


# CLASSE TILE

class Tile:
    def __init__(self, surf, solid_walls, breakable_walls, pushable_walls):
        self.enters = {}
        self.objects = {}
        self.teleporters = {}
        self.tile_map = surf
        self.solid_walls = solid_walls
        self.brekable_walls = breakable_walls
        self.pushable_walls = pushable_walls

    def _add_enter(self, x, y, name):
        self.enters[name] = (x, y)

    def _add_solid_walls(self, name, x, y, surf):
        wall = Wall((x, y), surf, self.solid_walls)
        key = f"solid_{name}_{x}_{y}"
        self.objects[key] = wall

    def _add_breakable_walls(self, name, x, y, surf):
        wall = Wall((x, y), surf, self.brekable_walls)
        key = f"breakable_{name}_{x}_{y}"
        self.objects[key] = wall

    def _add_pushable_walls(self, name, x, y, surf):
        wall = Wall((x, y), surf, self.pushable_walls)
        key = f"pushable_{name}_{x}_{y}"
        self.objects[key] = wall   
    
    def _add_teleporter(self, name, teleporter, x, y):
        teleporter.rect.topleft = (x, y)
        self.teleporters[name] = teleporter

    def _draw(self, screen, camera):
        screen.blit(self.tile_map, (-camera.position.x, -camera.position.y))
        for obj in self.objects.values():
            screen.blit(obj.image, camera.apply(obj.rect))


# CLASSE PLAYER

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, name, game, groups, collision_groups):
        super().__init__(groups)
        self.collision_groups = collision_groups
        self.game = FakeGame()

        self.base_titles = FakeTilesheet("", 50, 50, 1, 1 )         #portfolio des sprites
        test_img = pygame.Surface((50, 50))
        test_img.fill((0, 0, 255))
        self.animations = {
            "down_sp": [test_img],
            "up_sp": [test_img],
            "left_sp": [test_img],
            "right_sp": [test_img],
            "down": [test_img],
            "up": [test_img],
            "left": [test_img],
            "right": [test_img],
        }                                  #les sprites
        self.moving =False

        self.frame_index = 0
        self.statut = 'down_sp'
        self.sp_statut = ['up_sp', 'down_sp', 'left_sp', 'right_sp']    #les sprites statiques
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (50,50))

        self.name = name
        self.money = 0

        self.player_stat = {
            "life" : 10,
            "attack" : 10,
            "armor" : 10,
            "magic armor" : 10,
            "magic" : 10,
            "speed" : 10
            }
        
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.hitbox = self.rect.copy().inflate(0, 0)
        self.speed =200

    #regarde si le personnage est immobile ou en mouvement (utile notament pour savoir quelle sprite charger)
    def _check_sprite(self):
        if self.statut not in self.sp_statut:
            self.moving = True
        else:
            self.moving = False
    
    #change le sprite du joueur (pour animer un déplacement)
    def _animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.statut]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][int(self.frame_index)], (50,50))

    #regarde les input de déplacement du joueur et modifie les paramètre de déplacement en fonction
    def _input(self, actions):
        self.direction.y = 0
        self.direction.x = 0

        #déplacement en y (haut, bas)
        if actions['move up']:
            self.statut = 'up'
            self.direction.y -= 1
        elif actions['move down']:
            self.statut = 'down'
            self.direction.y = 1

        #déplacement en x (gauche, droite)
        if actions['move left']:
            self.statut = 'left'
            self.direction.x -= 1
        elif actions['move right']:
            self.statut = 'right'
            self.direction.x = 1

    #transforme les sprite de mouvement en sprite statique
    def _get_statut(self):
        if self.direction.magnitude() == 0:
            self.statut = self.statut.split('_')[0] + '_sp'
            self.moving = False

    #permet de déplacé la position du joueur et sa hitbox
    def _move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        #déplacement horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self._collision("horizontal")

        #déplacement vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self._collision("vertical")

        #mise à jour du rect (affichage)
        self.rect.center = self.hitbox.center

    #regarde si le joueur rencontre un obstacle et retourne en arrière si c'est la cas
    def _collision(self, direction):
        for sprite in self.collision_groups._sprites():
            if hasattr(sprite, "hitbox"):
                if self.hitbox.colliderect(sprite.hitbox):

                    if direction == "horizontal":
                        if self.direction.x > 0:  # droite
                            self.hitbox.right = sprite.hitbox.left
                        elif self.direction.x < 0:  # gauche
                            self.hitbox.left = sprite.hitbox.right
                        self.pos.x = self.hitbox.centerx

                    if direction == "vertical":
                        if self.direction.y > 0:  # bas
                            self.hitbox.bottom = sprite.hitbox.top
                        elif self.direction.y < 0:  # haut
                            self.hitbox.top = sprite.hitbox.bottom
                        self.pos.y = self.hitbox.centery
    
    #update l'ensemble des fonctions de déplacements du joueur pour créer une animation fluide
    def update(self, dt):
        self._input(self.game.actions)
        self._get_statut()
        self._check_sprite()
        self._move(dt)
        self._animate(dt)

    def _get_Name(self):
        return self.name
    
    def _get_Money(self):
        return self.money
    
    def _get_stat(self, stat):
        return self.player_stat[stat]
    
    def _set_stat(self, stat, change):
        self.player_stat[stat]+=change
    
    def _get_pos(self, coo):
        if coo == 0 : 
            return self.pos.x
        if coo == 1 :
            return self.pos.y
    
# CLASSE CAMERA

class Camera:
    def __init__(self, screen_width, screen_height):
        self.position = pygame.math.Vector2()
        self.screen_width = screen_width
        self.screen_height = screen_height

        # limites de la map
        self.map_width = 1000
        self.map_height = 1000

    def update(self, player):
        # centre la caméra sur le joueur
        self.position.x = player.rect.centerx - self.screen_width // 2
        self.position.y = player.rect.centery - self.screen_height // 2

        # empêche la caméra de sortir de la map
        self.position.x = max(0, min(self.position.x, self.map_width - self.screen_width))
        self.position.y = max(0, min(self.position.y, self.map_height - self.screen_height))

    def apply(self, rect):
        # retourne un rect décalé par la caméra
        return rect.move(-self.position.x, -self.position.y)


# PROGRAMME DE TEST

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
solid_walls = pygame.sprite.Group()
breakable_walls = pygame.sprite.Group()
pushable_walls = pygame.sprite.Group()

# SUPER GROUP

collision_groups = Collision_groups(solid_walls, breakable_walls, pushable_walls)

# MAP
map_surface = pygame.Surface((1000, 1000))
map_surface.fill((80, 180, 80))
tile = Tile(map_surface, solid_walls, breakable_walls, pushable_walls)

# MUR
wall_surface = pygame.Surface((100, 100))
wall_surface.fill((120, 60, 20))
tile._add_solid_walls("mur", 300, 200, wall_surface)

wall_surface = pygame.Surface((100, 100))
wall_surface.fill((120, 60, 20))
tile._add_solid_walls("mur", 500, 200, wall_surface)

wall_surface = pygame.Surface((100, 100))
wall_surface.fill((120, 60, 20))
tile._add_solid_walls("mur", 300, 500, wall_surface)

# JOUEUR
player = Player((100, 100), "Test", None, all_sprites, collision_groups)

# CAMERA
camera = Camera(800, 600)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # INPUT
    keys = pygame.key.get_pressed()
    player.game.actions = {
        'move up': keys[pygame.K_UP],
        'move down': keys[pygame.K_DOWN],
        'move left': keys[pygame.K_LEFT],
        'move right': keys[pygame.K_RIGHT],
    }

    # UPDATE
    all_sprites.update(dt)
    camera.update(player)

    # DRAW
    tile._draw(screen, camera)
    screen.blit(player.image, camera.apply(player.rect))

    pygame.display.flip()

pygame.quit()