import pygame
from item import Item

class Equipement(Item):
    def __init__(self, id, name, picture, attack, defense, magic, magic_defense, speed):
        self.id = id
        self.name = name
        self.picture = picture
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.magic_defense = magic_defense
        self.speed = speed

    def _get_Stat_(self, stat):
        if (stat == "attack"):
            return self.attack
        elif (stat == "defense"):
            return self.defense
        elif (stat == "magic"):
            return self.magic
        elif (stat == "magic_defense"):
            return self.magic_defense
        elif (stat == "speed"):
            return self.speed