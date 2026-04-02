import pygame
import config
import player

class Camera : 

    def __init__(self):
        self.x_cam = 0
        self.y_cam = 0
        self.x_min = 0
        self.y_min = 0
        self.x_max = 0
        self.y_max = 0

    def _update_cam(self, scree_height, screen_widht):
        if self.x_cam > self.x_min and self.x_cam < self.x_max:
            x_cam = 0