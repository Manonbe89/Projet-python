import pygame

class Fight_Entity:

    def __init__(self, name, combat_sprite, statistic, items):
        self.name = name
        self.statistic = statistic
        self.combat_sprite = combat_sprite
        self.items = items
        self.max_life = self._get_stat("life")

    def _get_stat(self, stat):
        return self.statistic[stat]

    def _set_stat(self, stat, change):
        self.statistic[stat] += change

    def _get_sprite(self):
        return self.combat_sprite
    
    def _get_objects(self):
        return self.objects
    
    def _get_max_life(self):
        return self.max_life
    
    def _clone(self):
        return Fight_Entity(
            self.name,
            self.combat_sprite,
            self.statistic.copy(),
            self.items
        )
    
    def is_dead(self):
        return self._get_stat("life") <= 0