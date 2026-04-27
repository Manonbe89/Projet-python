import pygame

pygame.init()                           #lance pygame
clock = pygame.time.Clock()
screen = pygame.display.set_mode((500, 500))

class Item: 
    def __init__(self, id, name, usage, description, picture):
        self.id = id
        self.name = name
        self.usage = usage
        self.description = description
        self.picture = picture
        self.picture_load = pygame.image.load(picture).convert_alpha()


    def _get_Id(self):
        return self.id
    
    def _get_Name(self):
        return self.name
        
    def _get_Usage(self) : 
        return self.usage
    
    def _get_Description(self) :
        return self.description
    
    def _get_Picture(self) : 
        return self.picture_load
    
    def _set_Name(self, new_name):
        self.name = new_name
    