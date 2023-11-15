from player import Player
from location import Location
from character import Character
from map import Map


def play():
    """Interaction logic of the game."""
    # Initiates player, character, map and locations.
    player = Player()
    dracula_jr = Character("Dracula Jr.")
    castle_map = Map()
    hall = Location("hall", True, None, True, False, "You have reached the hall.",
                    ending_point=True, north_leads_to='lounge', west_leads_to='bathroom')
    garden = Location("garden", True, False, True, False, "",
                      starting_point=True, north_leads_to='cemetery', west_leads_to='lounge')
    cemetery = Location("cemetery", False, True, False, False, "",
                        south_leads_to='garden')
    lounge = Location("lounge", True, True, False, True, "",
                      north_leads_to='guest bedroom', south_leads_to='hall', east_leads_to='garden')
    guest_bedroom = Location("guest bedroom", False, True, True, False,
                             "", south_leads_to='lounge', west_leads_to='master bedroom')
    master_bedroom = Location("master bedroom", False, False, False, True,
                              "", east_leads_to='guest bedroom')
    bathroom = Location("bathroom", False, False, False, True, "",
                        east_leads_to='hall')

    # Sets initial location.
    player.set_location(garden)

    # main game logic
    # while... do...
    current_location = player.location
    dracula_jr.welcome_player(player.name)
    player.backpack.add("flower")
    castle_map.print_map()
    available_exits = player.location.get_available_exits()
    response = dracula_jr.get_player_response(available_exits)

    if response == "I":
        player.backpack.show_inventory()
        response = dracula_jr.get_player_response(available_exits)
    else:
        response = dracula_jr.check_player_response(response, current_location, available_exits)
        if response == 'N':
            location = current_location.get_north_leads_to()
            print(player.set_location(location))


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    play()
