import pygame
import Tilesheet
import Game


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, new_name, game, groups, collision_sprites):
        super().__init__(groups)
        self.collision_sprites = collision_sprites
        self.game = Game.Game()
        self.base_titles = Tilesheet("", 50, 50, 1, 1 )
        self.animations = {}
        self.moving =False
        self.frame_index = 0
        self.statut = 'down_sp'
        self.sp_statut = ['up_sp', 'down_sp', 'left_sp', 'right_sp']
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (64,64))
        self.name = new_name
        self.money = 0
        self.life = 10
        self.attack = 10
        self.armor = 10
        self.magic = 10
        self.magic_armor = 10
        self.stat_speed = 10
        self.game = game

        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed =200

    def _check_sprite(self):
        if self.statut not in self.sp_statut:
            self.moving = True
        else:
            self.moving = False
    
    def _animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.statut]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][int(self.frame_index)], (64,64))

    def _input(self, actions):
        if actions['move up']:
            self.statut = 'up'
            self.direction.y -= 1
        elif actions['move down']:
            self.statut = 'down'
            self.direction.y = 1
        else:
            self.direction.y = 0

        if actions['move left']:
            self.statut = 'left'
            self.direction.x -= 1
        elif actions['move right']:
            self.statut = 'right'
            self.direction.x = 1
        else:
            self.direction.x = 0

    def _get_statut(self):
        if self.direction.magnitude() == 0:
            self.statut = self.statut.split('_')[0] + '_sp'
            self.moving = False

    def _move(self, dt):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = round(self.pos.x)
        self._collision("horizontal")

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = round(self.pos.y)
        self._collision("vertical")

    def _collision(self, direction):
        for sprite in self.collision_sprites.sprites():
            if hasattr(sprite, "hitbox"):
                if sprite.hitbox.colliderect(self.rect):
                    if direction == "horizontal":
                        if self.direction.x > 0:
                            self.rect.right = sprite.hitbox.left
                        if self.direction.x < 0 : 
                            self.rect.left = sprite.hitbox.right
                        self.pos.x = self.rect.centerx

                    if direction == "vertical":
                        if self.direction.y > 0:
                            self.rect.right = sprite.hitbox.top
                        if self.direction.y < 0 : 
                            self.rect.left = sprite.hitbox.bottom
                        self.pos.y = self.rect.centery
    
    def update(self, dt):
        self._input(self.game.actions)
        self._get_statut()
        self._check_sprite()
        self._move(dt)
        self._animate(dt)

    def _get_Name(self):
        return self.name
    
    def _get_Money(self):
        return self.money
    
    def _get_Life(self):
        return self.life
    
    def _get_Attack(self):
        return self.attack
    
    def _getArmor(self):
        return self.armor
    
    def _getMagic(self):
        return self.magic
    
    def _getMagicArmor(self):
        return self.magic_armor
    
    def _getSpeed(self):
        return self.stat_speed
    
    def _getCurentSprite(self):
        return self.curent_sprite
    
    def _addLife(self, life_add):
        self.life += life_add

    def _addAttack(self, attack_add):
        self.atatck += attack_add

    def _addArmor(self, armor_add):
        self.armor += armor_add

    def _addMagic(self, magic_add):
        self.magic += magic_add

    def _addMagicArmor(self, magic_armor_add):
        self.magic_armor += magic_armor_add

    def _addSpeed(self, speed_add):
        self.speed += speed_add

    def _addMoney(self, monney_add):
        self.money +=monney_add