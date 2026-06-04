import pygame

class Fight_Menu :
    def __init__(self, entity):

        self.entity = entity
        self.font = pygame.font.Font(None, 36)

        # main menu
        self.main_options = [
            "Attaque",
            "Objet",
            "Fuir"
        ]
        self.main_index = 0

        # sub menu
        self.sub_options = []
        self.sub_index = 0

        self.in_sub_menu = False
        self.finished = False
        self.locked_action = None
        self.target = None
        self.selected_option = None

        self._update_sub_menu()

    def _update_sub_menu(self):

        current = self.main_options[self.main_index]

        if current == "Attaque":
            self.sub_options = ["Attaque physique", "Attaque magique"]

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
    
            if event.key == pygame.K_SPACE:
                option = self._get_current_option()
                if option in ("Attaque physique", "Attaque magique", "Objet", "Fuir"):
                    self.finished = True
                    self.selected_option = option

    def _get_current_option(self):
            if self.in_sub_menu and self.sub_options:
                return self.sub_options[self.sub_index]

            return self.main_options[self.main_index]
    
    def _get_selected_option(self):
        return self.selected_option
    
    def _get_entity(self):
        return self.entity
    
    def _get_target(self):
        return self.target
    
    def _reset(self):
        self.in_sub_menu = False
        self.finished = False
        self.locked_action = None
        self.main_index = 0
        self.sub_index = 0


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