import pygame
from Code.enemys.enemy import Enemy

#a class for each enemy
class Bat : 
    def __init__(self):
        self.name = "bat"
        self.size = 25
        self.path = 'Images/bat.png'
        self.loot = 0
        self.detection_range = 400
        self.speed = 100

    def _create_enemy(self, pos, groups, collision_groups):
        bat = Enemy(self.name, self.size, self.path, pos, self.loot, self.detection_range, self.speed, groups, collision_groups, "nothing")
        return bat

#the bestiary (have a example of each enemy for a smoother incorporation)
class Bestiary : 
    def __init__(self):
        self.bat = Bat()