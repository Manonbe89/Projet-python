import pygame
import config

class Camera : 

    def __init__(self):
        self.x_cam = 0
        self.y_cam = 0
        self.x_min = 0
        self.y_min = 0
        self.x_max = 800
        self.y_max = 800

    def _update_cam(self, scree_height, screen_widht, x_player, y_player):
        if x_player > self.x_min and x_player < self.x_max:
            self.x_cam = 0

        if y_player > self.y_min and y_player < self.y_max:
            self.y_cam = 0