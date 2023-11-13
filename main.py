from player import Player
from location import Location
from character import Character


def play():
    """Interaction logic of the game."""

    player = Player()
    dracula_jr = Character("Dracula Jr.")
    hall = Location("Hall", True, None, True, False, "",
                    ending_point=True)
    garden = Location("Garden", True, False, True, False, "",
                      starting_point=True)
    cemetery = Location("Cemetery", False, True, False, False, "")
    lounge = Location("Lounge", True, True, False, True, "")
    guest_bedroom = Location("Guest bedroom", False, True, True, False,
                             "")
    master_bedroom = Location("Master bedroom", False, False, False, False,
                              "")
    bathroom = Location("bathroom", False, False, False, True, "")

    player.set_location(garden)

    # while... do...
    current_location = player.location
    dracula_jr.welcome_player(player.name)
    available_exits = player.location.get_available_exits()
    response = dracula_jr.get_player_response(available_exits)
    dracula_jr.check_player_response(response, current_location, available_exits)


if __name__ == "__main__":
    play()
