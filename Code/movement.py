import pygame

class Movement :
    def __init__(self, pos, statut, im_statut, animations, speed, size):
        self.statut = statut
        self.im_statut = im_statut
        self.size = size
        self.animations = animations
        self.speed = speed
        
        self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (self.size,self.size))
        self.rect = self.image.get_rect(center = pos)
        self.direction = pygame.math.Vector2()
        self.pos = pos
        self.hitbox = self.rect.copy().inflate(0, 0)


    def _change_direction(self, direction) :
        self.direction = direction

    def _check_sprite(self):
        if self.statut not in self.im_statut:
            self.moving = True
        else:
            self.moving = False

    def _animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.statut]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][int(self.frame_index)], (self.size, self.size))

    def _get_statut(self):
        if self.direction.magnitude() == 0:
            self.statut = self.statut.split('_')[0] + '_im'
            self.moving = False

    def _move(self, dt, current_map):
        if self.direction.magnitude() > 0:
            self.direction = self.direction.normalize()

        #déplacement horizontal
        self.pos.x += self.direction.x * self.speed * dt
        self.hitbox.centerx = round(self.pos.x)
        self._collision("horizontal", current_map)

        #déplacement vertical
        self.pos.y += self.direction.y * self.speed * dt
        self.hitbox.centery = round(self.pos.y)
        self._collision("vertical", current_map)

        #mise à jour du rect (affichage)
        self.rect.center = self.hitbox.center

    def _collision(self, direction, current_map):
        for sprite in current_map._get_collision_group()._sprites():
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

    def _save_to_entity(self, entity):
        entity._update_data(self.frame_index, self.image, self.rect, self.direction, self.pos, self.hitbox)

    
    def update(self, dt, current_map):
            self._get_statut()
            self._check_sprite()
            self._move(dt, current_map)
            self._animate(dt)

    def _set_statut(self, statut):
        self.statut = statut
