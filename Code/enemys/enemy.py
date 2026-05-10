import pygame
from Code.player.tilesheet import Tilesheet
from Code.enemys.enemy_AI import Enemy_AI

class Enemy(pygame.sprite.Sprite) : 

    def __init__(self, name, size, path, pos, loot, detection_range, speed, groups, collision_groups):
        super().__init__(groups)
        self.name = name
        self.size = size
        self.enemy_stat = {
            "life" : 1,
            "attack" : 0,
            "armor" : 0,
            "magic armor" : 0,
            "magic" : 0,
            "speed" : 0
            }
        image = pygame.image.load(path).convert_alpha()
        self.animations = {"immobile_sp": [image],
                           "movement_sp": [image],
                           "combat_sp": [image]}
        self.moving =False
        self.statut = "immobile_sp"
        self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (self.size,self.size))
        self.rect = self.image.get_rect(center = pos)
        self.pos = pygame.math.Vector2(self.rect.center)
        self.direction = pygame.math.Vector2(self.rect.center)
        self.hitbox = self.rect.copy().inflate(0, 0)
        self.speed = speed
        self.detection_range = self.rect.copy().inflate(
            -self.rect.width * detection_range,
            -self.rect.height * detection_range
        )
        self.loot = loot
        self.enemy_AI = Enemy_AI()
        self.collision_groups = collision_groups
        
        
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
    
    def _get_loot(self):
        return self.loot
    
    def _set_direction(self, coo, dir):
        if coo == 0 :
            self.direction.x = 0 
            self.direction.x += dir
        if coo == 1 :
            self.direction.y = 0 
            self.direction.y += dir

    def _check_sprite(self):
        if self.statut == 'movement':
            self.moving = 1

    def _animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.statut]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][int(self.frame_index)], (self.size, self.size))

    def _get_statut(self):
        if self.direction.magnitude() == 0:
            self.statut = 'immobile_sp'
            self.moving = False

    def _move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        #déplacement horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self._collision("horizontal")

        #déplacement vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self._collision("vertical")

        #mise à jour du rect (affichage)
        self.rect.center = self.hitbox.center

    def _collision(self, direction):
        for sprite in self.collision_groups._sprites():
            if hasattr(sprite, "hitbox"):
                if self.hitbox.colliderect(sprite.hitbox):

                    if direction == "horizontal":
                        if self.direction.x > 0:  # droite
                            self.hitbox.right = sprite.hitbox.left
                        elif self.direction.x < 0:  # gauche
                            self.hitbox.left = sprite.hitbox.right
                        self.pos.x = self.hitbox.centerx

                    if direction == "vertical":
                        if self.direction.y > 0:  # bas
                            self.hitbox.bottom = sprite.hitbox.top
                        elif self.direction.y < 0:  # haut
                            self.hitbox.top = sprite.hitbox.bottom
                        self.pos.y = self.hitbox.centery

    def update(self, dt, state, player):
        if state == False:
            self.enemy_AI._update(player, self)
            self._get_statut()
            self._check_sprite()
            self._move(dt)
            self._animate(dt)
