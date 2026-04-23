import pygame

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

    def _show_quote(self, screen, font):
        box_color=(0, 0, 0)
        text_color=(255, 255, 255)
        # dimensions de la boîte
        width = screen.get_width()
        height = 120
        x = 0
        y = screen.get_height() - height

        # dessiner la boîte
        dialogue_rect = pygame.Rect(x, y, width, height)
        pygame.draw.rect(screen, box_color, dialogue_rect)

        # rendu du texte
        text_surface = font.render(f"{self.name} : {self.quote}", True, text_color)

        # position du texte
        text_x = x + 20
        text_y = y + 20

        screen.blit(text_surface, (text_x, text_y))
        