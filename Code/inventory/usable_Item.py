import pygame
from Code.inventory.item import Item

class Usable_Item (Item):
    def __init__(self, id, name, picture, usage):
        self.id = id
        self.name = name
        self.picture = picture
        self.usage = usage

    def _get_Usage_(self):
        return self.usage

    def _Use_Item_(self, life):
        uitem = Usable_Item()
        print("Vous utilisez :", uitem._get_Name_())
