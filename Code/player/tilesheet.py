import pygame

class Tilesheet:
    def __init__(self, file_name, tile_width, tile_height, rows, cols):
        # Chargement sécurisé
        try:
            self.image = pygame.image.load(file_name).convert_alpha()
        except:
            raise FileNotFoundError(f"Impossible de charger l'image : {file_name}")

        self.tile_table = []

        for y in range(rows):        # lignes
            row = []
            for x in range(cols):    # colonnes
                rect = (x * tile_width, y * tile_height, tile_width, tile_height)
                row.append(self.image.subsurface(rect))
            self.tile_table.append(row)

    def get_tile(self, row, col):
        return self.tile_table[row][col]
