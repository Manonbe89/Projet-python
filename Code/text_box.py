import pygame


class Text_Box:
    def __init__(self, text):
        self.text = text
        self.text_color = (255, 255, 255)
        self.box_color = (0, 0, 0)
        self.interline = 25
        self.char_per_line = 70
        self.affichage_text = []
        self._cut_text()

    def _show_text(self, screen, font):
        # dimensions de la boîte
        width = screen.get_width()
        height = 120
        x = 0
        y = screen.get_height() - height

        # dessiner la boîte
        dialogue_rect = pygame.Surface((width, height))
        dialogue_rect.fill(self.box_color)
        screen.blit(dialogue_rect, (x, y))

        # position du texte
        text_x = x + 20
        text_y = y + 20

        # rendu du texte
        for i in range(len(self.affichage_text)):
            text_surface = font.render(self.affichage_text[i], True, self.text_color)
            screen.blit(text_surface, (text_x, text_y +i*25))

    def _cut_text(self):
        text_size = len(self.text)
        char_per_line = 70
        position = 0
        while position < text_size:
            cut_text = self.text[position:position+char_per_line]
            if cut_text [-1] != " " and position+char_per_line < text_size:
                last_space = cut_text.rfind(" ")
                if last_space != -1:
                    cut_text = cut_text[:last_space]
                position += last_space + 1
            else :
                position += char_per_line
            self.affichage_text.append(cut_text)