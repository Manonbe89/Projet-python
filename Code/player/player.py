import pygame
from Code.action.action import Action
from Code.player.tilesheet import Tilesheet
from Code.movement import Movement

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, name, action, groups, collision_groups):
        super().__init__(groups)
        self.collision_groups = collision_groups
        self.action = Action()

        self.size = 100
        test_img = pygame.image.load("Images/Perso vue de devant.png").convert_alpha()
        self.animations = {"down_im": [pygame.image.load("Images/Perso vue de devant.png").convert_alpha()],
                           "up_im": [pygame.image.load("Images/Perso vue de derriere.png").convert_alpha()],
                           "left_im": [pygame.image.load("Images/Perso vue de profil gauche.png").convert_alpha()],
                           "right_im": [pygame.image.load("Images/Perso vue de profil droite.png").convert_alpha()],
                           "down": [test_img],
                           "up": [test_img],
                           "left": [pygame.image.load("Images/Perso vue de profil gauche marche.png").convert_alpha()],
                           "right": [pygame.image.load("Images/Perso vue de profil droite marche.png").convert_alpha()],}                                    #les sprites de mouvement
        self.moving =False

        self.frame_index = 0
        self.statut = 'down'
        self.im_statut = ['up_im', 'down_im', 'left_im', 'right_im']    #les sprites statiques
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (self.size, self.size))

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
        self.movement = Movement(self.pos, self.statut, self.im_statut, self.animations, self.speed, self.size, collision_groups)

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

    def update(self, dt, state):
        if state == False:
            self._input(self.action.actions)
            self.movement.update(dt)
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

    def _set_stat_table(self, table) : 
        self.player_stat = table

    def _set_money(self, money_add):
        self.money +=self.money_add
    
    def _get_pos(self, coo):
        if coo == 0 : 
            return self.pos.x
        if coo == 1 :
            return self.pos.y
        
    def _set_pos(self, x, y) :
        self.pos.x = x
        self.pos.y = y

        
