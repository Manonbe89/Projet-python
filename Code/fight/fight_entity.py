import pygame

class Fight_Entity:

    def __init__(self, name, combat_sprite, statistic, items, spells):
        self.name = name
        self.statistic = statistic
        self.combat_sprite = combat_sprite
        self.items = items
        self.spells = spells

    def _get_stat(self, stat):
        return self.statistic[stat]

    def _set_stat(self, stat, change):
        self.statistic[stat] += change

    def _get_sprite(self):
        return self.combat_sprite
    

    def _get_spells(self):
        return self.spells
    
    def _get_objects(self):
        return self.objects
