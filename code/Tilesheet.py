import pygame

class Tilesheet:
    def __init__(self, file_name, widht, heights, rows, cols):
        image = pygame.image.load(file_name).convert_alpha()
        self.title_table = []
        for title_x in range (0, cols):
            line = []
            self.title_table.append(line)
            for title_y in range (0, rows):
                rect = (title_x * widht, title_y * heights, widht, heights)
                line.append(image.subsurface(rect).convert_alpha())

    def get_title(self, x, y):
        return self.title_table[x][y]