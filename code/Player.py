import pygame
import Tilesheet
import Game


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, name, game, groups, collision_sprites):
        super().__init__(groups)
        self.collision_sprites = collision_sprites
        self.game = Game.Game()

        self.base_titles = Tilesheet("", 50, 50, 1, 1 )
        self.animations = {}
        self.moving =False

        self.frame_index = 0
        self.statut = 'down_sp'
        self.sp_statut = ['up_sp', 'down_sp', 'left_sp', 'right_sp']
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (50,50))

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
        self.hitbox = self.rect.copy().inflate(-20, -20)
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
        self.image = pygame.transform.scale(self.animations[self.statut][int(self.frame_index)], (50,50))

    def _input(self, actions):
        self.direction.y = 0
        self.direction.x = 0

        if actions['move up']:
            self.statut = 'up'
            self.direction.y -= 1
        elif actions['move down']:
            self.statut = 'down'
            self.direction.y = 1

        if actions['move left']:
            self.statut = 'left'
            self.direction.x -= 1
        elif actions['move right']:
            self.statut = 'right'
            self.direction.x = 1

    def _get_statut(self):
        if self.direction.magnitude() == 0:
            self.statut = self.statut.split('_')[0] + '_sp'
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
        for sprite in self.collision_sprites.sprites():
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
    
    def _get_stat(self):
        return self.player_stat