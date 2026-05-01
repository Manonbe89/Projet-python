import pygame
import sys
from Code.item.item import Item

pygame.init()   #initialisation de pygame


class Usable_Item (Item):
    def __init__(self, id, name, usage, description, picture):
        self.id = id
        self.name = name
        self.usage = usage
        self.description = description
        self.picture = picture
        self.picture_load = pygame.image.load(picture).convert_alpha()
        self.use_item = False       #booléen qui verifie si on a utilise un item
        self.dialogue_step = 0