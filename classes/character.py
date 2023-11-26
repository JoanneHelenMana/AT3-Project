from location import Location
from player import Player
import string




class Character:
    """Acts as interface."""
    def __init__(self, name, player):
        self.name = name
        self.player = player

    def welcome_player(self):
        """Welcomes the player at the beginning of the game. Describes instructions, help and allowed input."""
        print(f"Welcome, {self.player.name}")
        # expand welcome message
        # I for inventory
        # thorough instruction

    @staticmethod
    def get_player_response(exits):
        """Presents to the player the question 'What do you want to do?' and displays available exists.
        Returns the player's response."""
        exits_str = ""
        for direction in exits:
            exits_str = ', '.join(exits)

        response = input(f"What do you want to do? Exits: {exits_str}\n")

        return response

    def check_player_response(self, response):
        """."""

        def check_letters(value):
            for letter in value:
                if letter not in string.ascii_letters:
                    return False
            return True

        location = ""
        command = ""

        if check_letters(response) is False:
            return False

        elif len(response.upper()) == 1:
            if response.upper() == 'N':
                location = self.player.location.get_north_leads_to()

            elif response.upper() == 'S':
                location = self.player.location.get_south_leads_to()

            elif response.upper() == 'E':
                location = self.player.location.get_east_leads_to()

            elif response.upper() == 'W':
                location = self.player.location.get_west_leads_to()
            return 'is location'

        elif len(response) > 1:
            command = response
            return 'is command'

    def get_next_room(self, response):
        """."""
        if response.upper() == 'N':
            location = self.player.location.get_north_leads_to()

        elif response.upper() == 'S':
            location = self.player.location.get_south_leads_to()

        elif response.upper() == 'E':
            location = self.player.location.get_east_leads_to()

        elif response.upper() == 'W':
            location = self.player.location.get_west_leads_to()

        return location

    def inspect_item(self):
        """."""
        print('item inspected')

    def wrong_input(self):
        print(f'Wrong input. Try again, {self.player.name}')
