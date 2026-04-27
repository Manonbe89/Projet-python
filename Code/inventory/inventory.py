#import Equipement

class Inventory:
    def __init__(self):
        self.stuff = [] 
        self.consumable_Item = []
        self.usable_Item = []

#getters
    def _get_stuff(self):
        return self.stuff
    
    def _get_consumable_Item(self):
        return self.consumable_Item

    def _get_usable_Item(self):
        return self.usable_Item
    
#setters
    def _set_stuff(self, Item):
        self.stuff.append(Item)

    def _set_consumable_Item(self, Item):
        self.consumable_Item.append(Item)

    def _set_usable_Item(self, Item):
        self.usable_Item.append(Item)
