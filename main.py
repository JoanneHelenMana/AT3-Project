from player import Player
from location import Location


def play():
    player = Player()
    hall = Location("Hall", True, None, True, False, ending_point=True)
    garden = Location("Garden", True, False, True, False, starting_point=True)


if __name__ == "__main__":
    play()
