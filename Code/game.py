import pygame
#import config

class Game:

    def __init__(self):
        self.actions = {'move left': False, 
                        'move right': False, 
                        'move_up': False, 
                        'move down': False
                        } 