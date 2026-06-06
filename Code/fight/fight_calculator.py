import pygame
import random

class Fight_calculator:
    def __init__(self):
        pass

    def _execute_action(self, action, enemys, allies):
        finished = True
        if action._get_action_type() == "Attaque physique":
            self._attaque_physique(action)
            return finished

        elif action._get_action_type() == "Attaque magique":
            self._attaque_magique(action)
            return finished

        elif action._get_action_type() == "Fuir":
            finished = self._fuir(enemys, allies)
            return finished

        elif action._get_action_type() == "Objet":
            self._objet(action)
            return finished

    def _attaque_physique(self, action):
        dammage = action._get_user()._get_stat("attack") - action._get_user()._get_stat("armor")/2
        action._get_target()._set_stat("life",dammage)

    def _attaque_magique(self, action):
        dammage = action._get_user()._get_stat("magic") - action._get_user()._get_stat("magic armor")/2
        action._get_target()._set_stat("life",dammage)

    def _fuir(self, enemys, allies):
        enemys_speed = 0
        for enemy in enemys:
            enemys_speed += enemy._get_stat("speed")

        allies_speed = 0
        for ally in allies:
            allies_speed += ally._get_stat("speed")

        finished = False
        if allies_speed >= 2*enemys_speed:
            finished = True
        
        elif allies_speed >= enemys_speed:
            if random.random() < 0.66:
                finished = True

        elif enemys_speed >= 2*enemys_speed:
            if random.random() < 0.05:
                finished = True

        elif enemys_speed >= enemys_speed:
            if random.random() < 0.33:
                finished = True


        return finished

    def _objet(self, action):
        pass