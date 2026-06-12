import pygame
class Action:
    def __init__(self):
        self.actions = {}

    def _set_keys(self, keys):
        self.actions = {
            'move up': keys[pygame.K_UP],
            'move down': keys[pygame.K_DOWN],
            'move left': keys[pygame.K_LEFT],
            'move right': keys[pygame.K_RIGHT],
            'space': keys[pygame.K_SPACE]
        }
