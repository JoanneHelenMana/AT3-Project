from location import Location
from player import Player


class Character:
    """."""
    def __init__(self, name, player=Player):
        self.name = name
        self.player = player

    @staticmethod
    def welcome_player(player_name):
        """Welcomes the player at the beginning of the game. Describes instructions, help and allowed input."""
        print(f"Welcome, {player_name}")
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
        response.upper()

        return response

    def check_player_response(self, response):
        """."""
        location = None

        if response.upper() == 'N':
            location = self.player.location.get_north_leads_to()
            print('location changed to N leads to')

        elif response.upper() == 'S':
            location = self.player.location.get_south_leads_to()

        elif response.upper() == 'E':
            location = self.player.location.get_east_leads_to()

        elif response.upper() == 'W':
            location = self.player.location.get_west_leads_to()

        else:
            response.lower()

        if location is not None:
            self.player.set_location(location)

        return response

    def inspect_item(self):
        """."""
        print('item inspected')

    def wrong_input(self):
        print(f'Wrong input. Try again, {self.player.name}')
