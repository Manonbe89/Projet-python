import pygame

class Object : 

    def __init__(self):
        self.invisible_wall = pygame.image.load('Images\invisible_wall.png').convert_alpha()