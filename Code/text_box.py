import pygame

class Text_Box:
    def __init__(self, text):
        self.text = text
        self.text_color = (255, 255, 255)
        self.box_color = (0, 0, 0)
        self.interline = 25
        self.char_per_line = 70
        self.max_lines = 3          # nombre max de lignes affichables
        self.page = 0               # page actuelle
        self.affichage_text = []
        self._cut_text()

    def _get_current_lines(self):
        start = self.page * self.max_lines
        end = start + self.max_lines
        return self.affichage_text[start:end]

    def _has_next_page(self):
        return (self.page + 1) * self.max_lines < len(self.affichage_text)

    def _next_page(self):
        if self._has_next_page():
            self.page += 1

    def _reset(self):
        self.page = 0

    def _show_text(self, screen, font):
        width = screen.get_width()
        height = 120
        x = 0
        y = screen.get_height() - height

        dialogue_rect = pygame.Surface((width, height))
        dialogue_rect.fill(self.box_color)
        screen.blit(dialogue_rect, (x, y))

        text_x = x + 20
        text_y = y + 20

        lines = self._get_current_lines()

        for i, line in enumerate(lines):
            text_surface = font.render(line, True, self.text_color)
            screen.blit(text_surface, (text_x, text_y + i * self.interline))

    def _cut_text(self):
        text_size = len(self.text)
        char_per_line = self.char_per_line
        position = 0

        while position < text_size:
            cut_text = self.text[position:position+char_per_line]
            if cut_text[-1] != " " and position + char_per_line < text_size:
                last_space = cut_text.rfind(" ")
                if last_space != -1:
                    cut_text = cut_text[:last_space]
                position += last_space + 1
            else:
                position += char_per_line

            self.affichage_text.append(cut_text)
