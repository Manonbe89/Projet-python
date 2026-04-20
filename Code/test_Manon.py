import pygame
from inventory import Inventory
from player import Player
from usable_Item import Usable_Item
from collision_group import Collision_groups
from wall import Wall
from tile import Tile
from camera import Camera
from game import Game

pygame.init()

screen = pygame.display.set_mode((900,600))        #définition de la fenêtre  avant 1000 500
pygame.display.set_caption('jeux')                  #nom de la fenêtre
clock = pygame.time.Clock()

game = Game()
inventory = Inventory()

# GROUPES (pas exploité (sauf all_sprites) mais nécessaire pour faire des déplacements)
all_sprites = pygame.sprite.Group()
wall_group = pygame.sprite.Group()
solid_walls = pygame.sprite.Group()
breakable_walls = pygame.sprite.Group()
pushable_walls = pygame.sprite.Group()
collision_groups = Collision_groups(wall_group)

test_font = pygame.font.Font(None, 30)
text_surface = test_font.render('Bonjour héros', True,'White')
n=0

# MAP (nécessaire pour une caméra (et donc des déplacements de joueur optimal))
map_surface = pygame.Surface((4000, 4000))
map_surface.fill((80, 180, 80))
tile = Tile(map_surface, solid_walls, breakable_walls, pushable_walls)

#ma partie (test)
player = Player ((0,0), "truc", None, all_sprites, collision_groups)
uitem = Usable_Item (0, "épée du voyageur", 0, "attaquer")

while True:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        inventory._check_inventory_status(event)
        uitem._check_item_status_(event)

    # INPUT
    keys = pygame.key.get_pressed()
    player.game.actions = {
        'move up': keys[pygame.K_UP],
        'move down': keys[pygame.K_DOWN],
        'move left': keys[pygame.K_LEFT],
        'move right': keys[pygame.K_RIGHT],
        'space': keys[pygame.K_SPACE]
    }

    # DEPLACEMENT
    camera = Camera(4000, 4000)
    all_sprites.update(dt)
    camera._update(player)
    tile._draw(screen, camera)
    screen.blit(player.image, camera._apply(player.rect))

    inventory._display_inventory(screen)                            #affiche l'inventaire si la condition est respectée
    uitem._Use_Item_(player, uitem, screen, test_font)

    n=n+10
    pygame.display.flip()