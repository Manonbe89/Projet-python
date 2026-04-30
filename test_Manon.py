import pygame
from Code.game.game import Game
from Code.item.inventory import Inventory
from Code.item.item import Item
from Code.item.usable_Item import Usable_Item
from Code.map.camera import Camera
from Code.map.collision_group import Collision_groups
from Code.map.tile import Tile
from Code.map.wall import Wall
from Code.npc.npc import NPC
from Code.player.player import Player
from Code.player.interaction import Interaction

pygame.init()

screen = pygame.display.set_mode((800,600))        #définition de la fenêtre  avant 1000 500
pygame.display.set_caption('jeux')                  #nom de la fenêtre
clock = pygame.time.Clock()
game = Game()
inventory = Inventory()

# GROUPES (pas exploité (sauf all_sprites) mais nécessaire pour faire des déplacements)
all_sprites = pygame.sprite.Group()
solid_walls = pygame.sprite.Group()
breakable_walls = pygame.sprite.Group()
pushable_walls = pygame.sprite.Group()
npc_group = pygame.sprite.Group()

font = pygame.font.Font(None, 32)

# SUPER GROUP

collision_groups = Collision_groups(solid_walls, breakable_walls, pushable_walls, npc_group)

# MAP
map_surface = pygame.Surface((1000, 1000))
map_surface.fill((80, 180, 80))
tile = Tile(map_surface, solid_walls, breakable_walls, pushable_walls, npc_group)

# MUR
wall_surface = pygame.Surface((100, 100))
wall_surface.fill((120, 60, 20))
tile._add_solid_walls("mur", 300, 200, wall_surface)

wall_surface = pygame.Surface((100, 100))
wall_surface.fill((120, 60, 20))
tile._add_pushable_walls("mur", 500, 200, wall_surface)

wall_surface = pygame.Surface((100, 100))
wall_surface.fill((120, 60, 20))
tile._add_breakable_walls("mur", 300, 500, wall_surface)

# NPC
npc_surface = pygame.Surface((50, 50))
npc_surface.fill((255, 0, 0))
tile._add_npc("Numerobis", npc_surface, 500, 500, "Vous savez, moi je ne crois pas qu’il y ait de bonne ou de mauvaise situation. Moi, si je devais résumer ma vie aujourd’hui avec vous, je dirais que c’est d’abord des rencontres. Des gens qui m’ont tendu la main, peut-être à un moment où je ne pouvais pas, où j’étais seul chez moi.")

# JOUEUR
player = Player((100, 100), "Test", game, all_sprites, collision_groups)

# CAMERA
camera = Camera(800, 600, 1000, 1000)

# INTERACTION
interaction = Interaction(player)

#ma partie (test)
uitem = Usable_Item (None, "Rien", None, None, "Images/epee_2.png")
inventory._item_factory()

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        inventory._check_inventory_status(event)
        inventory._check_buttons(event)
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

    # UPDATE
    all_sprites.update(dt, interaction._get_state())
    camera._update(player)

    # DRAW
    tile._draw(screen, camera)
    screen.blit(player.image, camera._apply(player.rect))

    # INTERACTION
    interaction._interact_npc(npc_group, screen, font)

    inventory._display_inventory(screen, font)                            #affiche l'inventaire si la condition est respectée
    uitem._Use_Item_(player, screen, font, inventory)
    screen.blit(font.render("Stats : " + 
                                 "life = " + str(player._get_stat("life")) + " / " +
                                 "attack = " + str(player._get_stat("attack")) + " / " +
                                 "armor = " + str(player._get_stat("armor")) + " / " + 
                                 "magic armor = " + str(player._get_stat("magic armor")) + " / " + 
                                 "magic = " + str(player._get_stat("magic")) + " / " + 
                                 "speed = " + str(player._get_stat("speed"))  
                                 , True, (255, 255, 255)), (5, 550))

    pygame.display.flip()

pygame.quit()