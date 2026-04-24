import pygame
from Code.text_box import Text_Box

class NPC(pygame.sprite.Sprite):
    def __init__(self, name, surf, pos, quote, groups):
        super().__init__(groups)
        self.name = name
        self.image = surf
        self.rect = self.image.get_rect(topleft=pos)
        self.quote = quote

        self.hitbox = self.rect.copy().inflate(
            -self.rect.width * 0,
            -self.rect.height * 0
        )
        self.text_box = Text_Box(quote)

    def _show_quote(self, screen, font):
        self.text_box._show_text(screen, font)