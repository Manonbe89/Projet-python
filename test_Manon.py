import pygame
from Code.game.game import Game
from Code.item.consumable_Item import Consumable_Item
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
from Code.enemys.enemy import Enemy
from Code.enemys.bestiary import Bestiary

pygame.init()

screen = pygame.display.set_mode((900,600))        #définition de la fenêtre  avant 1000 500
pygame.display.set_caption('jeux')                  #nom de la fenêtre
clock = pygame.time.Clock()
game = Game()
inventory = Inventory()

# GROUPES (pas exploité (sauf all_sprites) mais nécessaire pour faire des déplacements)
all_sprites = pygame.sprite.Group()

font = pygame.font.Font(None, 32)

# MAP
map_surface = pygame.Surface((1000, 1000))
map_surface.fill((80, 180, 80))
tile = Tile(map_surface)

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
player = Player((100, 100), "Test", game, all_sprites, inventory)

# CAMERA
camera = Camera(900, 600, 1000, 1000)

# INTERACTION
interaction = Interaction(player)

#ma partie (test)
inventory._item_factory()
current_item = inventory._get_current_Item()
uitem = Usable_Item(None, "", "Rien", "", "Images/bombe_2.png")
citem = Consumable_Item(None, "", "Rien", "", "Images/bombe_2.png")
item = inventory._get_Item(9)

#enemy
bestiary = Bestiary()
tile._add_ennemy(bestiary.bat, 800, 800)

running = True
while running:
    dt = clock.tick(60) / 1000

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN :                           # vérifie si l'événement keydown s'est produit ou non
             if event.key == pygame.K_g :
                 inventory._obtain_item(item, screen, font)

        if interaction._get_world_state() == 'fight':
            fight = interaction._get_current_fight()
            fight._handle_event(event)  
                            
        inventory._check_inventory_status(event)
        inventory._check_buttons(event)
        current_item._check_item_status(event, inventory)

    if interaction._get_world_state() == 'world' : 
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
        all_sprites.update(dt, interaction._get_state(),tile)
        camera._update(player)

        # DRAW
        tile._draw(screen, camera, dt, player, interaction._get_state())
        screen.blit(player.image, camera._apply(player.rect))

        # INTERACTION
        interaction._interact_npc(tile.npc_group, screen, font)
        interaction._intercat_with_enemy(tile.enemy_group)

        current_item = inventory._get_current_Item()
        inventory._display_inventory(screen, font)                            #affiche l'inventaire si la condition est respectée
        inventory._display_item(screen, item)
        uitem._use_usable_Item(player, screen, font, inventory, current_item)
        citem._Use_consumable_Item(screen, font, current_item)
        screen.blit(font.render("Stats : " +                                                        #a enlever par la suite
                                    "life = " + str(player._get_stat("life")) + " / " +
                                    "attack = " + str(player._get_stat("attack")) + " / " +
                                    "armor = " + str(player._get_stat("armor")) + " / " + 
                                    "magic armor = " + str(player._get_stat("magic armor")) + " / " + 
                                    "magic = " + str(player._get_stat("magic")) + " / " + 
                                    "speed = " + str(player._get_stat("speed"))  
                                    , True, (255, 255, 255)), (5, 25))

        

    elif interaction._get_world_state() == 'fight':
        fight = interaction._get_current_fight()
        fight._draw(screen)
        if interaction._get_current_fight()._is_finished():
            interaction._set_world_state('world')
            tile._delete_an_enemy(interaction)

    pygame.display.flip()

pygame.quit()