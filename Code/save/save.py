import json

class Save() :
    def _init_(self) :
        None


    def _get_data(self, inventory) :
        current_item = str(inventory._get_current_Item())
        nb_current_item = str(inventory._get_nb_current_Item())
        item_status = str(inventory._get_item_status())
        data = {"current_item": current_item,
                "nb_current_item": nb_current_item,
                "item_status": item_status
                }
        with open("Code\save\save.json", "w") as file :
            json.dump(data, file, indent=4)


    #def _load(self) :





