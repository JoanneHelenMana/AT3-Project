from location import Location
from backpack import Backpack

class Character:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def welcome_player(player_name):
        print(f"Welcome, {player_name}")
        # expand welcome message
        # I for inventory
        # thorough instruction

    @staticmethod
    def get_player_response(exits):
        response = input(f"What do you want to do? Exits: {exits}\n")
        return response

    def check_player_response(self, response, player_location, exits):
        # I for inventory returns items in backpack
        if response in exits:
            pass
