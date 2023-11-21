from classes.backpack import Backpack
from classes.location import Location


class Player:
    """."""
    def __init__(self, location, name=None, backpack=None):
        self.location = location
        self.set_initial_location(self.location)

        if name is None:
            self.name = self.set_name()

        if backpack is None:
            self.backpack = self.create_backpack()

    @staticmethod
    def set_name():
        """Sets the player's name."""
        name = input(f"What's your name, player?\n")
        return name

    @staticmethod
    def create_backpack():
        """Creates the player's backpack."""
        backpack = Backpack()
        return backpack

    def set_location(self, location=Location):
        """Sets the current location of the player."""
        self.location = location
        return self.location

    def set_initial_location(self, location):
        self.location = location

    def get_location(self):
        """Returns player location."""
        return self.location
