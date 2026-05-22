import pygame

class Fight_Entity:

    def __init__(self, name, combat_sprite, statistic, items, spells):
        self.name = name
        self.statistic = statistic
        self.combat_sprite = combat_sprite
        self.items = items
        self.spells = spells

    def _get_stat(self, stat):
        return self.player_stat[stat]
    
    def _set_stat(self, stat, change):
        self.player_stat[stat]+=change

    def _get_sprite(self):
        return self.combat_sprite
