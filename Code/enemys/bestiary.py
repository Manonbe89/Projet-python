import pygame
from Code.enemys.enemy import Enemy

class Bat : 
    def __init__(self):
        self.name = "bat"
        self.size = 25
        self.path = 'Images/bat.png'
        self.loot = 0
        self.detection_range = 400
        self.speed = 100

    def _create_enemy(self, pos, groups):
        bat = Enemy(self.name, self.size, self.path, pos, self.loot, self.detection_range, self.speed, groups)
        return bat

class Bestiary : 
    def __init__(self):
        self.bat = Bat()