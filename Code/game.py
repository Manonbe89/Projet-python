import pygame
from Code.item.consumable_Item import Consumable_Item
from Code.item.inventory import Inventory
from Code.item.usable_Item import Usable_Item
from Code.map.collision_group import Collision_groups
from Code.player.player import Player
from Code.player.interaction import Interaction
from Code.enemys.bestiary import Bestiary
from Code.map.map import Map

class Game : 

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.solid_walls = pygame.sprite.Group()
        self.breakable_walls = pygame.sprite.Group()
        self.pushable_walls = pygame.sprite.Group()
        self.npc_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.player = Player((100, 100), "Test", self.all_sprites, self.collision_groups)
        self.collision_groups = Collision_groups(self.solid_walls, self.breakable_walls, self.pushable_walls, self.npc_group)
        self.interaction = Interaction(self.player)
        self.inventory = Inventory()
        self.uitem = Usable_Item(None, "", "Rien", "", "Images/bombe_2.png")
        self.citem = Consumable_Item(None, "", "Rien", "", "Images/bombe_2.png")
        self.current_item = self.inventory._get_current_Item()
        self.bestiary = Bestiary()
        self.screen = pygame.display.set_mode((900,600))
        self.clock = pygame.time.Clock()
        self.map = Map(self.solid_walls, self.breakable_walls, self.pushable_walls, self.npc_group, self.enemy_group)
        self.item = self.inventory._get_Item(9)

    def _game_loop(self):
        pygame.init()

        self.inventory._item_factory()
        pygame.display.set_caption('jeux')

        self.player._set_current_tile(self.map.bedroom._get_tile())
        running = True
        while running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.inventory._check_inventory_status(event)
            self.inventory._check_buttons(event)
            self.current_item._check_item_status(event, self.inventory)

            # INPUT
            keys = pygame.key.get_pressed()
            self.player.action._set_keys(keys)

            # UPDATE
            self.all_sprites.update(dt, self.interaction._get_state())
            self.currentmap.camera._update(self.player)

            # DRAW
            self.player.current_tile._draw(self.screen, self.currentmap.camera, dt, self.player, self.interaction._get_state())
            self.screen.blit(self.player.image, self.currentmap.camera._apply(self.player.rect))

            # INTERACTION
            self.interaction._interact_npc(self.npc_group, self.screen)

            self.inventory._display_inventory(self.screen)                            #affiche l'inventaire si la condition est respectée
            self.inventory._display_item(self.screen, self.item)
            self.uitem._use_usable_Item(self.player, self.screen, self.inventory, self.current_item)
            self.citem._Use_consumable_Item(self.screen, self.current_item)


            pygame.display.flip()
            pygame.quit()



