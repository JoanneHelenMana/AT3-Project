from classes.player import Player
from classes.location import Location
from classes.character import Character
from classes.map import Map


def play():
    """Interaction logic of the game."""
    # Initiate player, character, and map.
    player = Player()
    dracula_jr = Character("Dracula Jr.")
    castle_map = Map()

    # Instantiate locations.
    hall = Location("hall", True, None, True, False, "You have reached the hall.",
                    map_position="2,1", ending_point=True, north_leads_to='lounge', west_leads_to='bathroom')
    garden = Location("garden", True, False, True, False, "",
                      map_position="1,2", starting_point=True, north_leads_to='cemetery', west_leads_to='lounge')
    cemetery = Location("cemetery", False, True, False, False, "",
                        map_position="2,0", south_leads_to='garden')
    lounge = Location("lounge", True, True, False, True, "",
                      map_position="1,1", north_leads_to='guest bedroom', south_leads_to='hall', east_leads_to='garden')
    guest_bedroom = Location("guest bedroom", False, True, True, False,
                             map_position="0,1", south_leads_to='lounge', west_leads_to='master bedroom', description="")
    master_bedroom = Location("master bedroom", False, False, False, True,
                              map_position="0,0", east_leads_to='guest bedroom', description="")
    bathroom = Location("bathroom", False, False, False, True, "",
                        map_position="2,0", east_leads_to='hall')

    # Set initial location.
    if garden.starting_point is True:
        player.set_location(garden)

    # Game main logic.
    dracula_jr.welcome_player(player.name)
    player.backpack.add("flower")
    available_exits = player.location.get_available_exits()

    while True:
        response = dracula_jr.get_player_response(available_exits)
        if response == "I":
            player.backpack.show_inventory()
        else:
            break

    current_location = player.get_location()
    dracula_jr.check_player_response(player, available_exits, response)
    current_location = player.get_location()


if __name__ == "__main__":
    play()
