#import Equipement

class Inventory:
    def init(self):
        self.stuff = [] 
        self.consumable_Item = []
        self.usuable_Item = []

#+, msg puis syncronise

    def get_consumable_Item(self):
        return self.consumable_Item

    def get_usuable_Item(self):
        return self.usuable_Item
    
    def set_consumable_Item(self, Item):
        consumable_Item += Item

    def set_usuable_Item(self, Item):
        usuable_Item += Item

#test
try:
    inv = Inventory
    inv.set_consumable_Item("bracelet")
    print(inv.get_consumable_Item())

except TypeError as e:
    print(f"Erreur lors de la création de l'objet : {e}")   