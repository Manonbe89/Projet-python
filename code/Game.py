import pygame
import config

class Game:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.setmode((config.SCREEN_WIDTH, config.SCREEN_HEIGHT))
        pygame.display.set_caption("GAME")
        self.clock = pygame.time.Clock
        self.running, self.playing = True, False
        self.state_stack = []
        self.dt=0
        self.player = None

        self.actions = {'space': False, 'left': False, 'right': False, 'up': False, 'down' : False,
                        'move left': False, 'move right': False, 'move_up': False, 'move down': False,
                        'enter': False, 'left mousse': False, 'escape': False} 
        self.next_state = None
        self.faing = None
        self.alpha = 0
        sr = pygame.display.get_surface().get_rect()
        self.veil = pygame.Surface(sr.size)
        self.veil.fill((0,0,0))
        self.all_sprites = pygame.sprite.Group()
        self.load_states()

    def load_states(self):
        #self.title = Title(self, "Title")
        self.state_stack.append(self.title)