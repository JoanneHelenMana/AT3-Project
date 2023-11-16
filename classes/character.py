from location import Location
from item import Item


class Character:
    """."""
    def __init__(self, name):
        self.name = name

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
        return response

    def check_player_response(self, player, exits, response):
        """."""
        response.upper()
        if response == 'N':
            location = player.location.get_north_leads_to()

        elif response == 'S':
            location = player.location.get_south_leads_to()

        elif response == 'E':
            location = player.location.get_east_leads_to()

        elif response == 'W':
            location = player.location.get_west_leads_to()

        else:
            response.lower()

        if location is not None:
            player.set_location(location)

        return response

    def inspect_item(self):
        """."""
        pass

    @staticmethod
    def wrong_input(player_name):
        print(f'Wrong input. Try again, {player_name}')
