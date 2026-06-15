import pygame
from Code.action.action import Action
from Code.player.tilesheet import Tilesheet
from Code.movement import Movement
from Code.fight.fight_entity import Fight_Entity

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, name, groups):
        super().__init__(groups)
        self.action = Action()

        self.size = 100
        test_img = pygame.image.load("Images/Perso vue de devant.png").convert_alpha()
        img_down_idle = pygame.image.load("Images/Perso vue de devant.png").convert_alpha()
        img_up_idle = pygame.image.load("Images/Perso vue de derriere.png").convert_alpha()
        img_left_idle = pygame.image.load("Images/Perso vue de profil gauche.png").convert_alpha()
        img_right_idle = pygame.image.load("Images/Perso vue de profil droite.png").convert_alpha()
        img_left_move = pygame.image.load("Images/Perso vue de profil gauche marche.png").convert_alpha()
        img_right_move = pygame.image.load("Images/Perso vue de profil droite marche.png").convert_alpha()
        self.animations = {"down_im": [img_down_idle],
                           "up_im": [img_up_idle],
                           "left_im": [img_left_idle],
                           "right_im": [img_right_idle],
                           "down": [img_down_idle],
                           "up": [img_up_idle],
                           "left": [img_left_move, img_left_idle],
                           "right": [img_right_move, img_right_idle],}                                    #les sprites de mouvement
        self.moving =False

        self.frame_index = 0
        self.statut = 'down'
        self.im_statut = ['up_im', 'down_im', 'left_im', 'right_im']    #les sprites statiques
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (self.size, self.size))

        self.name = name
        self.money = 5

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
        self.movement = Movement(self.pos, self.statut, self.im_statut, self.animations, self.speed, self.size, self.size)
        self.fight_entity = Fight_Entity(self.name, self.animations["down_im"][0],self.player_stat)

        self.allies_nb = 1

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
    
    #update l'ensemble des fonctions de déplacements du joueur pour créer une animation fluide
    def _update_data(self, frame_index, image, rect, direction, pos, hitbox):
        self.frame_index = frame_index
        self.image = image
        self.rect = rect
        self.direction = direction
        self.pos = pos
        self.hitbox = hitbox

    def update(self, dt, state, current_map):
        if state == False:
            self._input(self.action.actions)
            self.movement._change_direction(self.direction)
            self.movement._set_statut(self.statut)
            self.movement.update(dt, current_map)
            self.movement._save_to_entity(self)

    def _get_Name(self):
        return self.name
    
    def _get_Money(self):
        return self.money
    
    def _get_stat(self, stat):
        return self.player_stat[stat]
    
    def _get_stat_table(self) : 
        return self.player_stat
    
    def _set_stat(self, stat, change):
        self.player_stat[stat]+=change

    def _replace_stat(self, stat, value):
        self.player_stat[stat] = value

    def _sync_from_fight_entity(self):
        self._replace_stat("life", self.fight_entity._get_stat("life"))

    def _set_stat_table(self, table) : 
        self.player_stat = table

    def _set_money(self, money_add):
        if self.money + money_add >= 0:
            self.money +=money_add
    
    def _get_pos(self, coo):
        if coo == 0 : 
            return self.pos.x
        if coo == 1 :
            return self.pos.y
        
    def _set_pos(self, x, y) :
        self.pos.x = x
        self.pos.y = y

    def _get_allies_nb(self):
        return self.allies_nb
        
