import pygame
from Code.enemys.enemy import Enemy

#a class for each enemy
class Bat : 
    def __init__(self):
        self.name = "bat"
        self.xsize = 50
        self.ysize = 24
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
        self.xsize = 40
        self.ysize = 30
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
        self.xsize = 50
        self.ysize = 30
        self.path = 'Images/serpent.png'
        self.loot = 2
        self.detection_range = 400
        self.speed = 50

    def _create_enemy(self, pos, groups, map, number):
        enemy = Enemy(self.name, self.xsize, self.ysize, self.path, pos, self.loot, self.detection_range, self.speed, groups, map, number)
        enemy._set_stat(10,6,5,5,1,5)
        return enemy
    
class Dark_hero :
    def __init__(self):
        self.name = "dark_hero"
        self.xsize = 100
        self.ysize = 100
        self.path = 'Images/boss final.png'
        self.loot = 100
        self.detection_range = 0
        self.speed = 0

    def _create_enemy(self, pos, groups, map, number):
        enemy = Enemy(self.name, self.xsize, self.ysize, self.path, pos, self.loot, self.detection_range, self.speed, groups, map, number)
        enemy._set_stat(30,30,30,30,30,30)
        return enemy
    
class Buterflie :
    def __init__(self):
        self.name = "buterflie"
        self.xsize = 78
        self.ysize = 72
        self.path = 'Images/papillon.png'
        self.loot = 50
        self.detection_range = 0
        self.speed = 0

    def _create_enemy(self, pos, groups, map, number):
        enemy = Enemy(self.name, self.xsize, self.ysize, self.path, pos, self.loot, self.detection_range, self.speed, groups, map, number)
        enemy._set_stat(15,15,15,15,15,15)
        return enemy

class Golem :
    def __init__(self):
        self.name = "buterflie"
        self.xsize = 124
        self.ysize = 168
        self.path = 'Images/golem.png'
        self.loot = 50
        self.detection_range = 0
        self.speed = 0

    def _create_enemy(self, pos, groups, map, number):
        enemy = Enemy(self.name, self.xsize, self.ysize, self.path, pos, self.loot, self.detection_range, self.speed, groups, map, number)
        enemy._set_stat(15,15,15,15,15,15)
        return enemy


#the bestiary (have a example of each enemy for a smoother incorporation)
class Bestiary : 
    def __init__(self):
        self.bat = Bat()
        self.slime = Slime()
        self.snake = Snake()
        self.dark_hero = Dark_hero()
        self.butterflie = Buterflie()
        self.golem = Golem()