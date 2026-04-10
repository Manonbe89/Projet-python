import pygame

class Player:
    def __init__(self, new_name):
        self.name = new_name
        self.money = 0
        self.life = 10
        self.attack = 10
        self.armor = 10
        self.magic = 10
        self.magic_armor = 10
        self.speed = 10

    def __getName__(self):
        return self.name
    
    def __getMoney__(self):
        return self.money
    
    def __getLife__(self):
        return self.life
    
    def __getAttack__(self):
        return self.attack
    
    def __getArmor__(self):
        return self.armor
    
    def __getMagic__(self):
        return self.magic
    
    def __getMagicArmor__(self):
        return self.magic_armor
    
    def __getSpeed__(self):
        return self.speed
    
    def __getCurentSprite__(self):
        return self.curent_sprite
    
    def __addLife__(self, life_add):
        self.life += life_add

    def __addAttack__(self, attack_add):
        self.atatck += attack_add

    def __addArmor__(self, armor_add):
        self.armor += armor_add

    def __addMagic__(self, magic_add):
        self.magic += magic_add

    def __addMagicArmor__(self, magic_armor_add):
        self.magic_armor += magic_armor_add

    def __addSpeed__(self, speed_add):
        self.speed += speed_add

    def __addMoney__(self, monney_add):
        self.money +=monney_add
