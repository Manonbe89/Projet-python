import pygame
from Code.item.consumable_Item import Consumable_Item
from Code.item.inventory import Inventory
from Code.item.usable_Item import Usable_Item
from Code.player.player import Player
from Code.player.interaction import Interaction
from Code.map.map import Map
from Code.map.teleportation import Teleportation
from Code.save.save import Save

class Game : 

    def __init__(self):
        self.all_sprites = pygame.sprite.Group()
        self.inventory = Inventory()
        self.inventory._item_factory()
        self.player = Player((100, 100), "Test", self.all_sprites, self.inventory)
        self.interaction = Interaction(self.player)
        self.uitem = Usable_Item(None, "", "Rien", "", "Images/bombe_2.png")
        self.citem = Consumable_Item(None, "", "Rien", "", "Images/bombe_2.png")
        self.screen = pygame.display.set_mode((900,600))
        self.clock = pygame.time.Clock()
        self.map = Map()
        self.save = Save()
        self.teleportation = Teleportation()
        self.save._load_data(self.screen, self.inventory, self.player, self.map)
        self._game_loop()

    def _game_loop(self):

        pygame.display.set_caption('jeux')

        running = True
        while running:
            dt = self.clock.tick(60) / 1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN :                          # vérifie si l'événement keydown s'est produit ou non
                    if event.key == pygame.K_g :
                        self.inventory._obtain_item(self.inventory._get_Item(6), self.screen)

                if self.interaction._get_world_state() == 'fight':
                    fight = self.interaction._get_current_fight()
                    fight._handle_event(event)

                self.current_item = self.inventory._get_current_Item()
                self.inventory._check_inventory_status(event)
                self.inventory._check_buttons(event)
                self.current_item._check_item_status(event, self.inventory)
                self.save._check_buttons(event)

            #SAVE
            self.save._display_menu(self.screen)
            self.save._get_data(self.inventory, self.player, self.map)

            # INPUT
            if not self.save._get_state_menu():
                if self.interaction._get_world_state() == 'world':
                    keys = pygame.key.get_pressed()
                    self.player.action._set_keys(keys)

                    #Map
                    self.current_map = self.map._get_current_map()
                    self.teleportation._teleportation(self.player, self.map, self.screen)
                    
                    # UPDATE
                    self.all_sprites.update(dt, self.interaction._get_state(), self.current_map)
                    self.current_map.camera._update(self.player)

                    # DRAW
                    self.current_map._draw(self.screen, dt, self.player, self.interaction._get_state())
                    self.screen.blit(self.player.image, self.current_map.camera._apply(self.player.rect))

                    # INTERACTION
                    self.interaction._interact(self.current_map.enemy_group, self.current_map.npc_group, self.screen)

                    self.inventory._display_inventory(self.screen)                            #affiche l'inventaire si la condition est respectée
                    self.inventory._display_item(self.screen)
                    self.uitem._use_usable_Item(self.player, self.screen, self.inventory, self.current_item)
                    self.citem._Use_consumable_Item(self.screen, self.current_item)

                elif self.interaction._get_world_state() == 'fight':
                    fight = self.interaction._get_current_fight()
                    fight._draw(self.screen)
                    if self.interaction._get_current_fight()._is_finished():
                        self.current_map._delete_an_enemy(self.interaction)
                        self.interaction._return_to_world()


            pygame.display.flip()



