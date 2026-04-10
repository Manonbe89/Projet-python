import pygame

# Classe de calcul de la camera
class Camera:
    def __init__(self, screen_width, screen_height):
        self.position = pygame.math.Vector2()   # décalage de la caméra sur la map
        self.screen_width = screen_width
        self.screen_height = screen_height

        # limites de la map (peut etre à mettre en parametre si on fait des maps de taille différentes)
        self.map_width = 1000
        self.map_height = 1000

    def _update(self, player):
        # centre la caméra sur le joueur
        self.position.x = player.rect.centerx - self.screen_width // 2
        self.position.y = player.rect.centery - self.screen_height // 2

        # empêche la caméra de sortir de la map en prenant comme décalage : 
        # - le min de la limite supérieur et de la position du décalage (empeche d'etre plus grand que la limite supérieur)
        # - le max entre la limite inférieur et la position du décalage (empèche d'etre plus petit que la limite inférieur)
        # rmq : si la limite supérieur est prise au premier min on auras max(limite supérieur, 0 (limite inférieur)) ce qui donneras toujours la limite supérieur : c'est cohérent
        self.position.x = max(0, min(self.position.x, self.map_width - self.screen_width))
        self.position.y = max(0, min(self.position.y, self.map_height - self.screen_height))

    def _apply(self, rect):
        # retourne le rect décalé de l'inverse du décalage (car si on se décale vers le haut il faut que l'objet aille vers le bas)
        return rect.move(-self.position.x, -self.position.y)