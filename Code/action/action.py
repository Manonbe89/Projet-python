import pygame
class Action:
    def __init__(self):
        self.keys
        self.actions = {
            'move up': self.keys[pygame.K_UP],
            'move down': self.keys[pygame.K_DOWN],
            'move left': self.keys[pygame.K_LEFT],
            'move right': self.keys[pygame.K_RIGHT],
            'space': self.keys[pygame.K_SPACE]
        }

    def _set_keys(self, keys):
        self.keys = keys