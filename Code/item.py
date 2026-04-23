import pygame

pygame.init()                           #lance pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

class Item: 
    def __init__(self, id, name, picture):
        self.id = id
        self.name = name
        self.picture = picture

    def _get_Name_(self):
        return self.name
    
    def _set_Name(self, new_name):
        self.name = new_name

    def _get_Id_(self):
        return self.id
    
    def _display_Picture_(self, picture, screen):
        while(True):
            for event in pygame.event.get():        #permet de sortir de la fenetre
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
            screen.blit(picture, (0, 0))            #met l'image en 0 0
            pygame.display.update()                 #met a jour l'image
            clock.tick(30)                          #dit de s'actualiser tt les 30 ticks
