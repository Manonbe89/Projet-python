from pydoc import text
import re
import pygame

class Text_Box:
    def __init__(self, text):
        self.text = text
        self.text_color = (255, 255, 255)
        self.box_color = (0, 0, 0)
        self.interline = 25
        self.char_per_line = 70
        self.max_lines = 3

        self.pages = []   # liste de pages, chaque page = liste de lignes
        self.page = 0

        self._cut_text()

    def _get_current_lines(self):
        if 0 <= self.page < len(self.pages):
            return self.pages[self.page]
        return []

    def _has_next_page(self):
        return self.page + 1 < len(self.pages)

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

    def _wrap_text(self, text):
            lines = []
            position = 0
            text_size = len(text)

            while position < text_size:
                cut = text[position:position + self.char_per_line]

                if position + self.char_per_line < text_size and cut[-1] != " ":
                    last_space = cut.rfind(" ")
                    if last_space != -1:
                        cut = cut[:last_space]
                        position += last_space + 1
                    else:
                        position += self.char_per_line
                else:
                    position += self.char_per_line

                lines.append(cut.strip())

            return lines
    
    def _cut_text(self):

        self.pages = []
        self.page = 0

        sentences = re.split(r'(?<=[.!?]) +', self.text)
        sentences = [s.strip() for s in sentences if s.strip()]

        current_sentences = []
        current_lines = []

        for sentence in sentences:
            candidate_text = (" ".join(current_sentences + [sentence])).strip()
            candidate_lines = self._wrap_text(candidate_text)

            if len(candidate_lines) <= self.max_lines or not current_sentences:
                current_sentences.append(sentence)
                current_lines = candidate_lines
            else:
                self.pages.append(current_lines)
                current_sentences = [sentence]
                current_lines = self._wrap_text(sentence)

        if current_lines:
            self.pages.append(current_lines)