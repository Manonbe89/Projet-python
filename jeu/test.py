import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((1000,500))
pygame.display.set_caption('jeux')
clock = pygame.time.Clock()

test_surface = pygame.image.load('graphics/portrait.png')
test_font = pygame.font.Font(None, 30)
text_surface = test_font.render('Bonjour héros', True,'White')
n=0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.blit(test_surface,(n,n))
    pygame.display.update()
    n=n+10
    clock.tick(30)
