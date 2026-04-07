import pygame
import config

class Camera:
    def __init__(self, screen_width, screen_height):
        self.position = pygame.math.Vector2()
        self.screen_width = screen_width
        self.screen_height = screen_height

        # limites de la map
        self.map_width = 1000
        self.map_height = 1000

    def update(self, player):
        # centre la caméra sur le joueur
        self.position.x = player.rect.centerx - self.screen_width // 2
        self.position.y = player.rect.centery - self.screen_height // 2

        # empêche la caméra de sortir de la map
        self.position.x = max(0, min(self.position.x, self.map_width - self.screen_width))
        self.position.y = max(0, min(self.position.y, self.map_height - self.screen_height))

    def apply(self, rect):
        # retourne un rect décalé par la caméra
        return rect.move(-self.position.x, -self.position.y)