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

    #retourne les lignes de la page courante
    def _get_current_lines(self):
        if 0 <= self.page < len(self.pages):
            return self.pages[self.page]
        return []

    #vérifie s'il y a une page suivante
    def _has_next_page(self):
        return self.page + 1 < len(self.pages)

    #passe à la page suivante si elle existe
    def _next_page(self):
        if self._has_next_page():
            self.page += 1

    #reinitialise le dialogue à la première page
    def _reset(self):
        self.page = 0

    #affiche la page courante du dialogue sur l'écran
    def _show_text(self, screen, font):
        width = screen.get_width()
        height = 120
        x = 0
        y = screen.get_height() - height

        #dessine le rectangle de dialogue
        dialogue_rect = pygame.Surface((width, height))
        dialogue_rect.fill(self.box_color)
        screen.blit(dialogue_rect, (x, y))

        text_x = x + 20
        text_y = y + 20

        lines = self._get_current_lines()   #récupère les lignes de la page courante

        #affiche chaque ligne de texte de la page courante
        for i, line in enumerate(lines):
            text_surface = font.render(line, True, self.text_color)
            screen.blit(text_surface, (text_x, text_y + i * self.interline))

    #divise le texte en lignes en fonction du nombre de caractères par ligne et des espaces
    def _wrap_text(self, text):
        lines = []
        position = 0
        text_size = len(text)

        #tant qu'il reste des caractères à traiter, on coupe le texte en fonction du nombre de caractères par ligne
        while position < text_size:
            cut = text[position:position + self.char_per_line]  #coupe le texte à partir de la position actuelle jusqu'à la limite de caractères par ligne

            #si le dernier caractère n'est pas un espace, on cherche le dernier espace pour éviter de couper un mot
            if position + self.char_per_line < text_size and cut[-1] != " ":
                last_space = cut.rfind(" ")
                if last_space != -1:
                        cut = cut[:last_space]
                        position += last_space + 1
                else:
                        position += self.char_per_line
            else:
                position += self.char_per_line

            lines.append(cut.strip())   #ajoute la ligne coupée à la liste des lignes, en supprimant les espaces superflus

        return lines #retourne la liste des lignes coupées pour le texte donné
    
    #divise le texte en pages en fonction du nombre de lignes maximum par page et des phrases
    def _cut_text(self):
        #reset des pages et de la page courante
        self.pages = []
        self.page = 0

        #divise le texte en phrases en utilisant les ponctuations comme séparateurs
        sentences = re.split(r'(?<=[.!?]) +', self.text)
        sentences = [s.strip() for s in sentences if s.strip()] #filtre les phrases vides après le découpage

        current_sentences = []
        current_lines = []

        #pour chaque phrase, on essaie de l'ajouter à la page courante et on vérifie si le nombre de lignes dépasse le maximum autorisé
        for sentence in sentences:
            candidate_text = (" ".join(current_sentences + [sentence])).strip()
            candidate_lines = self._wrap_text(candidate_text)

            # si ça tient dans max_lines, on garde sur la même page
            if len(candidate_lines) <= self.max_lines or not current_sentences:
                current_sentences.append(sentence)
                current_lines = candidate_lines
            
            #sinon, on ajoute la page courante à la liste des pages et on commence une nouvelle page avec la phrase actuelle
            else:
                self.pages.append(current_lines)
                current_sentences = [sentence]
                current_lines = self._wrap_text(sentence)

        #gère la dernière page
        if current_lines:
            self.pages.append(current_lines)