import string

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
                             map_position="0,1", south_leads_to='lounge', west_leads_to='master bedroom',
                             description="")
    master_bedroom = Location("master bedroom", False, False, False, True,
                              map_position="0,0", east_leads_to='guest bedroom', description="")
    bathroom = Location("bathroom", False, False, False, True, "",
                        map_position="2,0", east_leads_to='hall')

    # Set initial location.
    if garden.starting_point is True:
        player.set_location(garden)

    # Game main logic starts.
    dracula_jr.welcome_player(player.name)
    player.backpack.add("vase")
    player.backpack.add("flower")

    while True:
        while True:
            available_exits = player.location.get_available_exits()
            response = dracula_jr.get_player_response(available_exits)
            if response == "I":     # I = inventory
                player.backpack.show_inventory()
            else:
                break

        while True:
            checked_response = dracula_jr.check_player_response(player, available_exits, response)
            if checked_response is not string.ascii_letters:
                dracula_jr.wrong_input(player.name)
            else:
                dracula_jr.inspect_item()


if __name__ == "__main__":
    play()
