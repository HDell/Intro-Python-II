# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room

class Player:

    def __init__(self, room, inventory=[]):
        self.room = room
        self.inventory = inventory

    def pick_up(self, item):
        if len(self.room.items) > 0:
            for l_item in self.room.items: #rsh enumerate
                if l_item.name == item:
                    self.inventory.append(l_item)
                    self.room.items.remove(l_item)
                    return
            print("Item doesn't exist.")
        else:
            print("There are no items in the room.")

    def drop(self, item):
        if len(self.inventory) > 0:
            for l_item in self.inventory:
                if l_item.name == item:
                    self.room.items.append(l_item)
                    self.inventory.remove(l_item)
                    return
            print("Item doesn't exist.")
        else:
            print("There are no items in your inventory.")

    def __str__(self):
        print(self.room.items)
        if len(self.room.items) > 0:
            text = "Your location is: " + self.room.name + ".\n" + self.room.description + "\nItems:" 
            for item in self.room.items:
                text += f"{item.name} {item.description}\n"
            return text
        else:
            return "Your location is: " + self.room.name + ".\n" + self.room.description + "\nThere are no items of interest here."
        
