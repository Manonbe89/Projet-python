import pygame
from Code.Game.game import Game
from Code.Player.tilesheet import Tilesheet

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, name, game, groups, collision_groups):
        super().__init__(groups)
        self.collision_groups = collision_groups
        self.game = Game()

        self.picture = "C:/Users/manon/Documents/Projet python S4/Frames/Perso vue de devant_2.png"
        self.test_picture = pygame.image.load(self.picture).convert_alpha()
        self.base_titles = Tilesheet(self.picture, 100, 100, 1, 1 )         #portfolio des sprites
        self.animations = {"down_sp": [self.test_picture],
                           "up_sp": [self.test_picture],
                           "left_sp": [self.test_picture],
                           "right_sp": [self.test_picture],
                           "down": [self.test_picture],
                           "up": [self.test_picture],
                           "left": [self.test_picture],
                           "right": [self.test_picture],}                                    #les sprites de mouvement
        self.moving =False

        self.frame_index = 0
        self.statut = 'down_sp'
        self.sp_statut = ['up_sp', 'down_sp', 'left_sp', 'right_sp']    #les sprites statiques
        self.image = pygame.transform.scale(self.animations[self.statut][self.frame_index], (100, 100))

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

    #regarde si le personnage est immobile ou en mouvement (utile notament pour savoir quelle sprite charger)
    def _check_sprite(self):
        if self.statut not in self.sp_statut:
            self.moving = True
        else:
            self.moving = False
    
    #change le sprite du joueur (pour animer un déplacement)
    def _animate(self, dt):
        self.frame_index += 4*dt
        if self.frame_index >= len(self.animations[self.statut]):
            self.frame_index = 0
        self.image = pygame.transform.scale(self.animations[self.statut][int(self.frame_index)], (100, 100))

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

    #transforme les sprite de mouvement en sprite statique
    def _get_statut(self):
        if self.direction.magnitude() == 0:
            self.statut = self.statut.split('_')[0] + '_sp'
            self.moving = False

    #permet de déplacé la position du joueur et sa hitbox
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

    #regarde si le joueur rencontre un obstacle et retourne en arrière si c'est la cas
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
    
    #update l'ensemble des fonctions de déplacements du joueur pour créer une animation fluide
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
    
    def _get_stat(self, stat):
        return self.player_stat[stat]
    
    def _set_stat(self, stat, change):
        self.player_stat[stat]+=change
    
    def _get_pos(self, coo):
        if coo == 0 : 
            return self.pos.x
        if coo == 1 :
            return self.pos.y
        
    def _set_money(self, money_add):
        self.money +=self.money_add