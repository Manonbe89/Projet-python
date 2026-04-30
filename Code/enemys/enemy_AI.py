import pygame
from Code.enemys.enemy import Enemy

class Enemy_AI:
    def __init__(self, enemy):
        self.enemy = enemy

    def _update(self, player):
        detection_range = self.enemy._get_detection_range()