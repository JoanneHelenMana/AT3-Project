from classes.backpack import Backpack
from classes.map import Map


class Player:
    """The player of the game. It is mainly used to move the player around the castle's rooms."""
    def __init__(self, location, name=None, backpack=None):
        self.location = location
        self.set_initial_location(self.location)
        self.map = Map()

        if name is None:
            self.name = self.set_name()

        if backpack is None:
            self.backpack = self.create_backpack()

    @staticmethod
    def set_name():
        """Sets the player's name."""
        name = input(f"What's your name, stranger?\n")
        return name

    @staticmethod
    def create_backpack():
        """Creates the player's backpack."""
        backpack = Backpack()
        return backpack

    def set_location(self, location):
        """Sets the current location of the player."""
        self.location = location
        if self.location.visited is False:
            self.location.visited = True
            self.map.update_map(location)
        print(self.location.get_description())
        if self.location.item is not None and self.backpack.in_backpack(self.location.item.name) == -1:
            print(self.location.item.message_in_location)

        # self.map.print_map()      if uncommented, it will print and update the map as the player moves around
        return self.location

    def set_initial_location(self, location):
        """Sets the initial location of the player."""
        self.location = location

    def get_location(self):
        """Returns player location."""
        return self.location

    def print_description(self):
        """Prints location description to console."""
        print(self.location.get_description())
