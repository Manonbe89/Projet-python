import pygame
from Code.enemys.enemy import Enemy

#a class for each enemy
class Bat : 
    def __init__(self):
        self.name = "bat"
        self.xsize = 100
        self.ysize = 48
        self.path = 'Images/BAT.png'
        self.loot = 2
        self.detection_range = 400
        self.speed = 100

    def _create_enemy(self, pos, groups, map, number):
        enemy = Enemy(self.name, self.xsize, self.ysize, self.path, pos, self.loot, self.detection_range, self.speed, groups, map, number)
        enemy._set_stat(10,6,5,5,1,5)
        return enemy
    
class Slime : 
    def __init__(self):
        self.name = "bat"
        self.xsize = 80
        self.ysize = 60
        self.path = 'Images/slime.png'
        self.loot = 2
        self.detection_range = 400
        self.speed = 25

    def _create_enemy(self, pos, groups, map, number):
        enemy = Enemy(self.name, self.xsize, self.ysize, self.path, pos, self.loot, self.detection_range, self.speed, groups, map, number)
        enemy._set_stat(10,6,5,5,1,5)
        return enemy
    
class Snake : 
    def __init__(self):
        self.name = "bat"
        self.xsize = 100
        self.ysize = 60
        self.path = 'Images/serpent.png'
        self.loot = 2
        self.detection_range = 400
        self.speed = 50

    def _create_enemy(self, pos, groups, map, number):
        enemy = Enemy(self.name, self.xsize, self.ysize, self.path, pos, self.loot, self.detection_range, self.speed, groups, map, number)
        enemy._set_stat(10,6,5,5,1,5)
        return enemy

#the bestiary (have a example of each enemy for a smoother incorporation)
class Bestiary : 
    def __init__(self):
        self.bat = Bat()
        self.slime = Slime()
        self.snake = Snake()