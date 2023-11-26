import string
from classes.player import Player
from classes.location import Location
from classes.character import Character
from classes.map import Map
import time


def play():
    """Interaction logic of the game."""
    # Instantiate locations. Max = 9
    hall = Location("hall", True, None, True, False, "You have reached the hall.",
                    map_position="2,1", ending_point=True, north_leads_to='lounge', west_leads_to='bathroom')
    garden = Location("garden", True, False, True, False, "You have reached the garden.",
                      map_position="1,2", starting_point=True, north_leads_to='cemetery', west_leads_to='lounge')
    cemetery = Location("cemetery", False, True, False, False, "You have reached the cemetery.",
                        map_position="2,0", south_leads_to='garden')
    lounge = Location("lounge", True, True, False, True, "You have reached the lounge.",
                      map_position="1,1", north_leads_to='guest bedroom', south_leads_to='hall', east_leads_to='garden')
    guest_bedroom = Location("guest bedroom", False, True, True, False,
                             map_position="0,1", south_leads_to='lounge', west_leads_to='master bedroom',
                             description="You have reached the guest bedroom.")
    master_bedroom = Location("master bedroom", False, False, False, True,
                              map_position="0,0", east_leads_to='guest bedroom', description="You have reached the "
                                                                                             "master bedroom.")
    bathroom = Location("bathroom", False, False, False, True, "You have reached the bathroom.",
                        map_position="2,0", east_leads_to='hall')
    locations = [garden, cemetery]
    inaccessible_map_positions = ["1,0", "2,2"]

    while True:
        # Initiate player, character, and map.
        starting_point = ''
        if garden.starting_point is True:
            starting_point = garden

        player = Player(starting_point)
        dracula_jr = Character("Dracula Jr.", player)
        castle_map = Map(inaccessible_map_positions)

        # Instantiate items.

        # Set initial location.
        if garden.starting_point is True:
            player.set_location(garden)

        # Game main logic starts.
        dracula_jr.welcome_player()
        print(dracula_jr.player.location.name)
        player.backpack.add("vase")
        player.backpack.add("flower")

        while True:
            while True:
                inventory = "I"
                available_exits = player.location.get_available_exits()
                response = dracula_jr.get_player_response(available_exits)

                if response.upper() == inventory:
                    # Display inventory
                    player.backpack.show_inventory()
                else:
                    # Assess player's input other than 'inventory'
                    break

            checked_response = dracula_jr.check_player_response(response)

            if checked_response is False:
                # Bad input
                print(f'Wrong input. Try again, {player.name}')
                continue

            elif checked_response == 'is location':
                # Response is a direction: N, S, W, E
                new_room = dracula_jr.get_next_room(response)
                for location in locations:
                    # Matches input to Location
                    if new_room == location.name:
                        new_room = location
                        if Location.__instancecheck__(new_room) is True:
                            player.set_location(new_room)
                break
            elif checked_response == 'is command':
                # Response is a command
                dracula_jr.inspect_item()
                break

        play_again = input('Would you like yo play again?')
        if play_again == 'yes':
            continue
        else:
            print(f'No worries, {player.name}. See you next time.')
            time.sleep(3)
            quit()


if __name__ == "__main__":
    play()
