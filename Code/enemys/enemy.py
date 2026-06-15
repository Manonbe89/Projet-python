import pygame
from Code.player.tilesheet import Tilesheet
from Code.enemys.enemy_AI import Enemy_AI
from Code.movement import Movement
from Code.fight.fight_entity import Fight_Entity

class Enemy(pygame.sprite.Sprite) : 

    def __init__(self, name, xsize, ysize, path, pos, loot, detection_range, speed, groups, map, number):
        super().__init__(groups)
        self.name = name
        self.number = number
        self.xsize = xsize
        self.ysize = ysize
        self.enemy_stat = {
            "life" : 10,
            "attack" : 1,
            "armor" : 1,
            "magic armor" : 1,
            "magic" : 1,
            "speed" : 1
            }
        self.pos = pos
        self.speed = speed
        image = pygame.image.load(path).convert_alpha()
        self.animations = {"sprite_im": [image],
                           "sprite": [image],
                           "combat_sp": pygame.transform.scale(image,(self.xsize,self.ysize))}
        self.statut = "sprite"
        self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (self.xsize,self.ysize))
        self.rect = self.image.get_rect(center = pos)
        self.hitbox = self.rect.copy()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(self.rect.center)
        self.im_statut = ["sprite_im"]
        self.detection_range = self.rect.copy().inflate(
            -self.rect.width * detection_range,
            -self.rect.height * detection_range
        )
        self.loot = loot
        self.enemy_AI = Enemy_AI()
        self.movement = Movement(self.pos, self.statut, self.im_statut, self.animations, self.speed, self.xsize, self.ysize)
        self.fight_entity = Fight_Entity(self.name, self.animations["combat_sp"], self.enemy_stat)
        self.map = map
        
        
    def _set_stat(self, life, attack, armor, magic_armor, magic, speed):
        self.enemy_stat["life"] = life
        self.enemy_stat["attack"] = attack
        self.enemy_stat["armor"] = armor
        self.enemy_stat["magic_armor"] = magic_armor
        self.enemy_stat["magic"] = magic
        self.enemy_stat["speed"] = speed

    def _get_stat(self, stat):
        return self.enemy_stat[stat]
    
    def _mod_stat(self, stat, change):
        self.enemy_stat[stat]+=change

    def _get_pos(self, coo) :
        if coo == 0 : 
            return self.pos.x
        if coo == 1 :
            return self.pos.y
    
    def _get_detection_range(self):
        return self.detection_range
    
    def _get_loot(self):
        return self.loot
    
    def _set_direction(self, coo, dir):
        if coo == 0 :
            self.direction.x = 0 
            self.direction.x += dir
        if coo == 1 :
            self.direction.y = 0 
            self.direction.y += dir

    #update all the movement variable (because of the movemnt encapsulation)
    def _update_data(self, frame_index, image, rect, direction, pos, hitbox):
        self.frame_index = frame_index
        self.image = image
        self.rect = rect
        self.direction = direction
        self.pos = pos
        self.hitbox = hitbox

    def _get_hitbox(self):
        return self.hitbox
    
    def _get_number(self):
        return self.number

    #all the movement function
    def update(self, dt, state, player):
        if state == False:
            self.enemy_AI._update(player, self)
            self.movement._change_direction(self.direction)
            self.movement.update(dt, self.map)
            self.movement._save_to_entity(self)
