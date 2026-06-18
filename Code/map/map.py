import pygame
from Code.map.camera import Camera
from Code.map.tile import Tile
from Code.map.object import Object
from Code.enemys.bestiary import Bestiary


class Map : 

    def __init__(self):
        self.bedroom = Bedroom()
        self.first_village = First_Village()
        self.intersection = Intersection()
        self.left_path = Left_path()
        self.right_path = Right_path()
        self.dwarf_village = Dwarf_village()
        self.elf_village = Elf_village()
        self.current_map = self.bedroom._get_tile()
        self.name_current_map = 'bedroom'
        self.name_before_village = ''
    
    def _get_name_current_map(self) : 
        return self.name_current_map
    
    def _get_current_map(self) :
        return self.current_map
    
    def _set_current_map(self, name) :
        self.name_current_map = name
        if name == 'bedroom' : 
            self.current_map = self.bedroom._get_tile()

        elif name == 'first_village' :
            self.current_map = self.first_village._get_tile()

        elif name == 'intersection' :
            self.current_map = self.intersection._get_tile()
            self.name_before_village = 'intersection'
            
        elif name == 'left_path' :
            self.current_map = self.left_path._get_tile()

        elif name == 'right_path' :
            self.current_map = self.right_path._get_tile()

        elif name == 'dwarf_village' :
            self.current_map = self.dwarf_village._get_tile()
            self.name_before_village = 'dwarf_village'

        elif name == 'elf_village' : 
            self.current_map = self.elf_village._get_tile()
            self.name_before_village = 'elf_village'

        elif name == 'Donjon':
            self.current_map = self.donjon._get_tile()
    

class Bedroom() : 

    def __init__(self):
        self.name = 'bedroom'
        self.surf = pygame.image.load("Images/Chambre.png").convert_alpha()
        self.camera = Camera(900, 600, 500, 500)
        self.tile = Tile(self.surf, self.camera)
        self.bestiary = Bestiary()
        self.object = Object()
        self._create_map()

    def _create_map(self):
        table = pygame.transform.scale(self.object.invisible_wall, (130,135))
        bed = pygame.transform.scale(self.object.invisible_wall, (80,165))
        top_bordure = pygame.transform.scale(self.object.invisible_wall, (500,1))
        side_bordure = pygame.transform.scale(self.object.invisible_wall, (1,500))
        self.tile._add_solid_walls('table', 395, 235, table)
        self.tile._add_solid_walls('bed', 632, 60, bed)
        self.tile._add_solid_walls('top_bordure', 202,60, top_bordure)
        self.tile._add_solid_walls('bot_bordure', 202, 560, top_bordure)
        self.tile._add_solid_walls('left_bordure', 202,60, side_bordure)
        self.tile._add_solid_walls('right_bordure', 701,60, side_bordure)

    def _get_name_map(self) : 
        return self.name
    
    def _get_tile(self):
        return self.tile
    

class First_Village() : 

    def __init__(self):
        self.name = 'first_village'
        self.surf = pygame.image.load("Images/Map.png").convert_alpha()
        self.camera = Camera(900, 600, 1000, 1000)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self._create_map()

    def _create_map(self):
        house = pygame.transform.scale(self.object.invisible_wall, (170,140))
        top_bordure = pygame.transform.scale(self.object.invisible_wall, (450, 30))
        bot_bordure = pygame.transform.scale(self.object.invisible_wall, (1000, 30))
        side_bordure = pygame.transform.scale(self.object.invisible_wall, (30, 1000))
        self.tile._add_solid_walls('house', 90, 70, house)                      #top left
        self.tile._add_solid_walls('house', 670, 40, house)                     #top right
        self.tile._add_solid_walls('house', 390, 280, house)                    #middle
        self.tile._add_solid_walls('house', 160, 690, house)                    #bot left
        self.tile._add_solid_walls('house', 670, 520, house)                    #bot right
        self.tile._add_solid_walls('top_bordure', 0, 0, top_bordure)
        self.tile._add_solid_walls('top_bordure', 550, 0, top_bordure)
        self.tile._add_solid_walls('bot_bordure', 0, 970, bot_bordure)
        self.tile._add_solid_walls('left_bordure', 0, 0, side_bordure)
        self.tile._add_solid_walls('right_bordure', 970, 0, side_bordure)

        human = pygame.image.load("Images/humain.png").convert_alpha()
        self.tile._add_npc("Corentin",human,350, 30,"Savais tu que l'épée boost ton attaque, tu devrais essayer !")

    def _get_name_map(self) : 
        return self.name
    
    def _get_tile(self):
        return self.tile
    
class Intersection() :
    def __init__(self):
        self.name = 'intersection'
        self.surf = pygame.image.load("Images/Chemin_milieu.png").convert_alpha()
        self.camera = Camera(900, 600, 1000, 1000)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self._create_map()

    def _create_map(self):
        top_bordure = pygame.transform.scale(self.object.invisible_wall, (415, 30))
        side_bordure = pygame.transform.scale(self.object.invisible_wall, (30, 415))
        self.tile._add_solid_walls('top_bordure', 0, 0, top_bordure)
        self.tile._add_solid_walls('top_bordure', 585, 0, top_bordure)
        self.tile._add_solid_walls('bot_bordure', 0, 970, top_bordure)
        self.tile._add_solid_walls('bot_bordure', 585, 970, top_bordure)
        self.tile._add_solid_walls('left_bordure', 0, 0, side_bordure)
        self.tile._add_solid_walls('left_bordure', 0, 585, side_bordure)
        self.tile._add_solid_walls('right_bordure', 970, 0, side_bordure)
        self.tile._add_solid_walls('right_bordure', 970, 585, side_bordure)

    def _get_name_map(self) : 
        return self.name
    
    def _get_tile(self):
        return self.tile
    
class Left_path() :
     def __init__(self):
        self.name = 'left_path'
        self.surf = pygame.image.load("Images/Coin_gauche.png").convert_alpha()
        self.camera = Camera(900, 600, 1000, 1000)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self._create_map()
    
     def _create_map(self):
        top_bordure_1 = pygame.transform.scale(self.object.invisible_wall, (148, 30))
        top_bordure_2 = pygame.transform.scale(self.object.invisible_wall, (682, 30))
        left_bordure = pygame.transform.scale(self.object.invisible_wall, (30, 1000))
        bot_bordure = pygame.transform.scale(self.object.invisible_wall, (1000, 30))
        right_bordure_1 = pygame.transform.scale(self.object.invisible_wall, (30, 160))
        right_bordure_2 = pygame.transform.scale(self.object.invisible_wall, (30, 670))
        self.tile._add_solid_walls('top_bordure', 0, 0, top_bordure_1)
        self.tile._add_solid_walls('top_bordure', 318, 0, top_bordure_2)
        self.tile._add_solid_walls('left_bordure', 0, 0, left_bordure)
        self.tile._add_solid_walls('left_bordure', 0, 970, bot_bordure)
        self.tile._add_solid_walls('right_bordure', 970, 840, right_bordure_1)
        self.tile._add_solid_walls('right_bordure', 970, 0, right_bordure_2)

     def _get_name_map(self) : 
        return self.name
    
     def _get_tile(self):
        return self.tile
     

class Right_path() :
     def __init__(self):
        self.name = 'right_path'
        self.surf = pygame.image.load("Images/Coin_droit.png").convert_alpha()
        self.camera = Camera(900, 600, 1000, 1000)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self._create_map()
    
     def _create_map(self):
        top_bordure_2 = pygame.transform.scale(self.object.invisible_wall, (148, 30))
        top_bordure_1 = pygame.transform.scale(self.object.invisible_wall, (682, 30))
        right_bordure = pygame.transform.scale(self.object.invisible_wall, (30, 1000))
        bot_bordure = pygame.transform.scale(self.object.invisible_wall, (1000, 30))
        left_bordure_1 = pygame.transform.scale(self.object.invisible_wall, (30, 160))
        left_bordure_2 = pygame.transform.scale(self.object.invisible_wall, (30, 670))
        self.tile._add_solid_walls('top_bordure', 0, 0, top_bordure_1)
        self.tile._add_solid_walls('top_bordure', 852, 0, top_bordure_2)
        self.tile._add_solid_walls('left_bordure', 0, 0, left_bordure_2)
        self.tile._add_solid_walls('bot_bordure', 0, 970, bot_bordure)
        self.tile._add_solid_walls('right_bordure', 0, 840, left_bordure_1)
        self.tile._add_solid_walls('right_bordure', 970, 0, right_bordure)

     def _get_name_map(self) : 
        return self.name
    
     def _get_tile(self):
        return self.tile
     
class Dwarf_village() :
     def __init__(self):
        self.name = 'dwarf_village'
        self.surf = pygame.image.load("Images/Map_nain.png").convert_alpha()
        self.camera = Camera(900, 600, 1000, 1000)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self._create_map()
    
     def _create_map(self):
        house = pygame.transform.scale(self.object.invisible_wall, (160,180))
        top_bordure = pygame.transform.scale(self.object.invisible_wall, (450, 30))
        side_bordure = pygame.transform.scale(self.object.invisible_wall, (30, 1000))
        self.tile._add_solid_walls('house', 130, 40, house)                      #top left
        self.tile._add_solid_walls('house', 700, 20, house)                     #top right
        self.tile._add_solid_walls('house', 410, 280, house)                    #middle
        self.tile._add_solid_walls('house', 200, 670, house)                    #bot left
        self.tile._add_solid_walls('house', 690, 510, house)                    #bot right
        self.tile._add_solid_walls('top_bordure', 0, 0, top_bordure)
        self.tile._add_solid_walls('top_bordure', 550, 0, top_bordure)
        self.tile._add_solid_walls('top_bordure', 0, 970, top_bordure)
        self.tile._add_solid_walls('top_bordure', 550, 970, top_bordure)
        self.tile._add_solid_walls('left_bordure', 0, 0, side_bordure)
        self.tile._add_solid_walls('right_bordure', 970, 0, side_bordure)

        dwarf = pygame.image.load("Images/dwarf.png").convert_alpha()
        self.tile._add_npc('roi des nains', dwarf, 600, 900,"Aide nous aventurier il faut terasser le golem caché dans la grotte à la sorti du village !")

     def _get_name_map(self) : 
        return self.name
    
     def _get_tile(self):
        return self.tile
     
class Dwarf_village() :
     def __init__(self):
        self.name = 'dwarf_village'
        self.surf = pygame.image.load("Images/Map_nain.png").convert_alpha()
        self.camera = Camera(900, 600, 1000, 1000)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self._create_map()
    
     def _create_map(self):
        house = pygame.transform.scale(self.object.invisible_wall, (160,180))
        top_bordure = pygame.transform.scale(self.object.invisible_wall, (450, 30))
        side_bordure = pygame.transform.scale(self.object.invisible_wall, (30, 1000))
        self.tile._add_solid_walls('house', 130, 40, house)                      #top left
        self.tile._add_solid_walls('house', 700, 20, house)                     #top right
        self.tile._add_solid_walls('house', 410, 280, house)                    #middle
        self.tile._add_solid_walls('house', 200, 670, house)                    #bot left
        self.tile._add_solid_walls('house', 690, 510, house)                    #bot right
        self.tile._add_solid_walls('top_bordure', 0, 0, top_bordure)
        self.tile._add_solid_walls('top_bordure', 550, 0, top_bordure)
        self.tile._add_solid_walls('top_bordure', 0, 970, top_bordure)
        self.tile._add_solid_walls('top_bordure', 550, 970, top_bordure)
        self.tile._add_solid_walls('left_bordure', 0, 0, side_bordure)
        self.tile._add_solid_walls('right_bordure', 970, 0, side_bordure)

     def _get_name_map(self) :
         return self.name
    
     def _get_tile(self):
        return self.tile
     
class Donjon() :
    def __init__(self):
        self.name = 'Donjon'
        self.surf = pygame.image.load("Images/Donjon.png").convert_alpha()
        self.camera = Camera(900, 600, 1000, 1000)
        self.tile = Tile(self.surf, self.camera)
        self.object = Object()
        self.bestiary = Bestiary()
        self._create_map()
    
    def _create_map(self):

        top_bordure = pygame.transform.scale(self.object.invisible_wall, (450, 30))
        bot_bordure = pygame.transform.scale(self.object.invisible_wall, (1000, 30))
        side_bordure = pygame.transform.scale(self.object.invisible_wall, (30, 1000))

        self.tile._add_solid_walls('top_bordure', 0, 0, bot_bordure)
        self.tile._add_solid_walls('top_bordure', 550, 970, top_bordure)
        self.tile._add_solid_walls('bot_bordure', 0, 970, top_bordure)
        self.tile._add_solid_walls('left_bordure', 0, 0, side_bordure)
        self.tile._add_solid_walls('right_bordure', 970, 0, side_bordure)

        if map.before_village == 'dwarf_village' :
            golem = self.bestiary.golem
            self.tile._add_ennemy(golem, 500, 500, 1)

        elif map.before_village == 'elf_village' :
            butterflie = self.bestiary.butterflie
            self.tile._add_ennemy(butterflie, 500, 500, 1)

        elif map.before_village == 'intersection' :
            dark_hero = self.bestiary.dark_hero
            self.tile._add_ennemy(dark_hero, 500, 500, 1)

    def _get_name_map(self) :
        return self.name
    
    def _get_tile(self):
        return self.tile
     

class Elf_village() :
    None