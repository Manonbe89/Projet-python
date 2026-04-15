import pygame

#obstacle constituer d'un rectangle, d'une hitbox et d'un groupe (pour réunir tous les obstacles dans une meme liste)
class Wall(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)

        self.hitbox = self.rect.copy().inflate(
            -self.rect.width * 0.6,
            -self.rect.height * 0.75
        )
