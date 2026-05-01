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
        self.dialogue_step = 0
        self.use_item = False       #booléen qui verifie si on a utilise un item
        if self.picture != "" :
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
    
    def _get_dialogue_step(self) :
        return self.dialogue_step
    
    def _get_use_item(self) :
        return self.use_item
    
    def _set_Name(self, new_name):
        self.name = new_name

    def _check_item_status(self, event, inventory):
         if event.type == pygame.KEYDOWN :           # vérifie si l'événement keydown s'est produit ou non
              if event.key == pygame.K_u :           # vérifie si la touche "u" a été pressée
                   if not inventory._get_state() :
                        self.dialogue_step += 1

    