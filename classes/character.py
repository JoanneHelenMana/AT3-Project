from location import Location


class Character:
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
        if len(response) is 1:  # one character: N, S, W, or E

            if response.upper() == 'N':
                location = player.location.get_north_leads_to()

            elif response.upper() == 'S':
                location = player.location.get_south_leads_to()

            elif response.upper() == 'E':
                location = player.location.get_east_leads_to()

            elif response.upper() == 'W':
                location = player.location.get_west_leads_to()

            player.set_location(location)

        if len(response) > 1:
            pass
        # if valid sentence

        # else: prompt message
