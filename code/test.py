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


# CLASSE PLAYER

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, name, game, groups, collision_sprites):
        super().__init__(groups)
        self.collision_sprites = collision_sprites
        self.game = FakeGame()

        self.base_titles = FakeTilesheet("", 50, 50, 1, 1 )
        self.moving =False

        self.frame_index = 0
        self.statut = 'down_sp'
        self.sp_statut = ['up_sp', 'down_sp', 'left_sp', 'right_sp']

        # sprite de test
        test_img = pygame.Surface((50, 50))
        test_img.fill((255, 0, 150))
        self.animations = {
            "down_sp": [test_img],
            "up_sp": [test_img],
            "left_sp": [test_img],
            "right_sp": [test_img],
            "down": [test_img],
            "up": [test_img],
            "left": [test_img],
            "right": [test_img],
        }

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
        self.hitbox = self.rect.copy().inflate(-20, -20)
        self.speed =200

    def _check_sprite(self):
        if self.statut not in self.sp_statut:
            self.moving = True
        else:
            self.moving = False
    
    def _animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.statut]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][int(self.frame_index)], (50,50))

    def _input(self, actions):
        self.direction.y = 0
        self.direction.x = 0

        if actions['move up']:
            self.statut = 'up'
            self.direction.y -= 1
        elif actions['move down']:
            self.statut = 'down'
            self.direction.y = 1

        if actions['move left']:
            self.statut = 'left'
            self.direction.x -= 1
        elif actions['move right']:
            self.statut = 'right'
            self.direction.x = 1

    def _get_statut(self):
        if self.direction.magnitude() == 0:
            self.statut = self.statut.split('_')[0] + '_sp'
            self.moving = False

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

    def _collision(self, direction):
        for sprite in self.collision_sprites.sprites():
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
    
    def _get_stat(self):
        return self.player_stat
    
# CLASSE CAMERA

class Camera : 

    def __init__(self):
        self.x_cam = 0
        self.y_cam = 0
        self.x_min = 0
        self.y_min = 0
        self.x_max = 800
        self.y_max = 800

    def _update_cam(self, scree_height, screen_widht, x_player, y_player):
        if x_player > self.x_min and x_player < self.x_max:
            self.x_cam = x_player + screen_widht /2

        if y_player > self.y_min and y_player < self.y_max:
            self.y_cam = y_player + scree_height /2

# PROGRAMME DE TEST

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
collision_sprites = pygame.sprite.Group()

# MAP
map_surface = pygame.Surface((800, 600))
map_surface.fill((80, 180, 80))
tile = Tile(map_surface, collision_sprites)

# MUR
wall_surface = pygame.Surface((100, 100))
wall_surface.fill((120, 60, 20))
tile._add_object("mur", 300, 200, wall_surface)

# JOUEUR
player = Player((100, 100), "Test", None, all_sprites, collision_sprites)

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

    all_sprites.update(dt)
    tile._draw(screen)
    all_sprites.draw(screen)

    pygame.display.flip()

pygame.quit()
