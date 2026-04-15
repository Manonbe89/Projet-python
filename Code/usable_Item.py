import pygame
from item import Item
from player import Player

class Usable_Item (Item):
    def __init__(self, id, name, picture, usage):
        self.id = id
        self.name = name
        self.picture = picture
        self.usage = usage

    def _get_Usage_(self):
        return self.usage

    def _Use_Item_(self, player, uitem):
        print("Vous utilisez :", uitem._get_Name_())
        
        if (uitem._get_Name_() == "épée du voyageur"):
            player._set_stat("attack", 5)
            print ("Vous gagnez 5 points d'attaque")
