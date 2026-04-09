class Collision_groups : 
    # prend les différents groupe du super groupe en entré
    def __init__(self, *groups):
        self.groups = groups

    # copie les sprite des différents objet des différents groupe en evitant les doublons
    def _sprites(self):
        combined = set()
        for g in self.groups:
            combined.update(g.sprites())
        return list(combined)

    # permet l'itération (for x in Collision_groups)
    def __iter__(self):
        return iter(self.sprites())

    #permet d'utiliser la methode len(Collision_groups)
    def __len__(self):
        return len(self.sprites())