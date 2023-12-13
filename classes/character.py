from location import Location
from player import Player
from classes.item import Item
import string


class Character:
    """The game's character's other than the player. This class acts as the interface of the game."""
    def __init__(self, name, player):
        self.name = name
        self.player = player

    def welcome_player(self):
        """Welcomes the player at the beginning of the game. Describes instructions, help and allowed input."""
        print(f"Hello, {self.player.name}. My name is {self.name}\nMy father will be very, very upset to find you"
              f" in his house.\nIf you help me find the Gameboy he's taken from me, I will let you go and "
              f"not tell him about your intrusion.\nHelp me go around the castle to find my Gameboy and meet me "
              f"at the hall once you've found it.\nIf you try to leave the house before I have my Gameboy,"
              f" you won't be able to escape my father's teeth...\n")

    @staticmethod
    def get_player_response(exits):
        """Presents to the player the question 'What do you want to do?' and displays available exists.
        Returns the player's response."""
        exits_str = ""
        for direction in exits:
            exits_str = ', '.join(exits)

        response = input(f"What do you want to do? Exits: {exits_str}\n")

        return response

    @staticmethod
    def check_letters(value):
        for letter in value:
            if letter not in string.ascii_letters:
                if letter not in string.whitespace:
                    return False
        return True

    def check_player_response(self, response):
        """."""
        location = ""
        response = response.strip()

        if len(response) == 1:
            # Response is a direction (exit)
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
            if self.check_letters(response) is False:
                # Bad input
                return False

            elif self.check_letters(response) is True:
                # Response is a command
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

    def inspect_item(self, location, response):
        """."""
        words = response.split()
        if len(words) == 2:
            # Checks a two-word command for coincidence with item in location
            for word in words:
                if word == location.item.name:
                    return True    # Coincidence with item
            return False     # No coincidence with item

        elif len(words) != 2:
            # Command too long
            return False

    def wrong_input(self):
        """Prints a wrong input message to console."""
        print(f'Wrong input. Try again, {self.player.name}')

    def wrong_command(self):
        """Prints a wrong command message to console."""
        print(f'Wrong command. Try again.')

    def display_help(self):
        """Prints help message to console."""
        print(f"\nHelp:\nYour goal is to find Dracula Jr.'s Nintendo Flex, reach the hall and return it to him."
              f"You might be tempted to reach the hall and leave the castle, however, you'll lose the game that way"
              f"and will face the fatal Dracula's bite.\n\nTo navigate the rooms in the castle, use the available exits"
              f":\nN = north\nS = south\nW = west\nE = east\n\nYou can pick up items along your way using a two-word "
              f"command. If the item presented is a pen, enter 'take pen'. This will add the item to your backpack.\n"
              f"To check the items in your backpack, enter 'I'.\nFor help, enter 'H'.\n")

    def display_winning_message(self):
        print("You have won!")
        return

    def display_losing_message(self):
        print("You have lost!")
        return
