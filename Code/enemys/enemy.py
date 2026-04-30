import pygame

class Enemy(pygame.sprite.Sprite) : 

    def __init__(self, name, pos, detection_range, speed, tilesheet, groups):
        super().__init__(groups)
        self.name = name
        self.enemy_stat = {
            "life" : 10,
            "attack" : 0,
            "armor" : 0,
            "magic armor" : 0,
            "magic" : 0,
            "speed" : 0
            }
        self.animations = {"imobile_sp": tilesheet.get_tile(1,1),
                           "movement_sp": tilesheet.get_tile(1,2) }
        self.moving =False
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.hitbox = self.rect.copy().inflate(0, 0)
        self.speed = speed
        self.detection_range = detection_range
        
        
    def _set_stat(self, life, attack, armor, magic_armor, magic, speed):
        self.enemy_stat["life"] = life
        self.enemy_stat["attack"] = attack
        self.enemy_stat["armor"] = armor
        self.enemy_stat["magic_armor"] = magic_armor
        self.enemy_stat["magic"] = magic
        self.enemy_stat["speed"] = speed

    def _get_stat(self, stat):
        return self.enemy_stat[f"{stat}"]
    
    def _mod_stat(self, stat, change):
        self.enemy_stat[f"{stat}"]+=change

    def _get_pos(self, coo) :
        if coo == 0 : 
            return self.pos.x
        if coo == 1 :
            return self.pos.y
    
    def _get_detection_range(self):
        return self.detection_range
