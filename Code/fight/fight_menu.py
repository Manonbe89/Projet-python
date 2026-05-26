import pygame

class Fight_Menu :
    def __init__(self, entity):

        self.entity = entity
        self.font = pygame.font.Font(None, 36)

        # main menu
        self.main_options = [
            "Attaque",
            "Sort",
            "Objet",
            "Fuir"
        ]

        self.main_index = 0

        # sub menu
        self.sub_options = []
        self.sub_index = 0

        self.in_sub_menu = False

        self._update_sub_menu()

    def _update_sub_menu(self):

        current = self.main_options[self.main_index]

        if current == "Sort":
            self.sub_options = self.entity.spells

        elif current == "Objet":
            self.sub_options = self.entity.items

        elif current == "Attaque":
            self.sub_options = ["Attaque normale"]

        else:
            self.sub_options = []

        self.sub_index = 0

    def _handle_event(self, event):

        if event.type == pygame.KEYDOWN:

            if not self.in_sub_menu:

                if event.key == pygame.K_UP:
                    self.main_index -= 1
                    self.main_index %= len(self.main_options)
                    self._update_sub_menu()

                elif event.key == pygame.K_DOWN:
                    self.main_index += 1
                    self.main_index %= len(self.main_options)
                    self._update_sub_menu()

                elif event.key == pygame.K_RIGHT:
                    if self.sub_options:
                        self.in_sub_menu = True

            else:

                if event.key == pygame.K_UP:
                    self.sub_index -= 1
                    self.sub_index %= len(self.sub_options)

                elif event.key == pygame.K_DOWN:
                    self.sub_index += 1
                    self.sub_index %= len(self.sub_options)

                elif event.key == pygame.K_LEFT:
                    self.in_sub_menu = False

    def _draw(self, screen):
        menu_high = 420

        # main menu background
        pygame.draw.rect(screen,(40, 40, 40),(20, menu_high-20, 250, 180))

        # sub menu background
        pygame.draw.rect(screen,(60, 60, 60),(300, menu_high-20, 300, 180))

        # MAIN MENU
        for i, option in enumerate(self.main_options):

            if not self.in_sub_menu and i == self.main_index:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)

            text = self.font.render(option, True, color)
            screen.blit(text, (40, menu_high + i * 40))

        # SUB MENU
        for i, option in enumerate(self.sub_options):

            if self.in_sub_menu and i == self.sub_index:
                color = (255, 255, 0)
            else:
                color = (255, 255, 255)

            text = self.font.render(str(option), True, color)
            screen.blit(text, (320, menu_high + i * 40))