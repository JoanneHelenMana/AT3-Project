from classes.player import Player
from classes.location import Location
from classes.character import Character
from classes.item import Item
import time


def play():
    """Interaction logic of the game."""

    while True:
        # Instantiate items (5).
        book = Item('book', 'That book seems interesting', 'You have picked up a book')
        key = Item('key', 'That key seems interesting', 'You have picked up a key')
        lamp = Item('lamp', 'That lamp seems interesting', 'You have picked up a lamp')
        flower = Item('flower', 'That flower seems interesting', 'You have picked up a flower')
        nintendo_flex = Item('Nintendo Flex', 'That nintendo flex seems interesting', 'You have picked up a Nintendo Flex')
        items = [book, key, lamp, flower, nintendo_flex]

        # Instantiate locations (7).
        hall = Location("hall", True, False, True, False, "You have reached the hall.",
                        map_position="2,1", ending_point=True, north_leads_to='lounge', west_leads_to='bathroom')
        garden = Location("garden", True, False, True, False, "You are now in the garden.",
                          map_position="1,2", starting_point=True, north_leads_to='cemetery', west_leads_to='lounge', item=lamp)
        cemetery = Location("cemetery", False, True, False, False, "You have reached the cemetery.",
                            map_position="0,2", south_leads_to='garden')
        lounge = Location("lounge", True, True, False, True, "You have reached the lounge.",
                          map_position="1,1", north_leads_to='guest bedroom', south_leads_to='hall', east_leads_to='garden', item=book)
        guest_bedroom = Location("guest bedroom", False, True, True, False,
                                 map_position="0,1", south_leads_to='lounge', west_leads_to='master bedroom',
                                 description="You have reached the guest bedroom.")
        master_bedroom = Location("master bedroom", False, False, False, True,
                                  map_position="0,0", east_leads_to='guest bedroom', description="You have reached the "
                                  "master bedroom.", item=key)
        bathroom = Location("bathroom", False, False, False, True, "You have reached the bathroom.",
                            map_position="2,0", east_leads_to='hall', item=nintendo_flex)
        locations = [garden, cemetery, hall, lounge, guest_bedroom, master_bedroom, bathroom]

        # Initiate player, character, and map.
        starting_point = ''
        if garden.starting_point is True:
            starting_point = garden

        player = Player(starting_point)
        dracula_jr = Character("Dracula Jr.", player)

        # Game main logic starts.
        dracula_jr.welcome_player()

        # Set initial location.
        if garden.starting_point is True:
            player.set_location(garden)

        while True:
            inventory = "I"
            _help = "H"
            available_exits = player.location.get_available_exits()
            response = dracula_jr.get_player_response(available_exits)

            if response.upper() == inventory:
                # Display inventory
                player.backpack.show_inventory()
                continue

            if response.upper() == _help:
                # Display help
                dracula_jr.display_help()
                continue

            checked_response = dracula_jr.check_player_response(response)

            if checked_response is False:
                # Bad input
                dracula_jr.wrong_input()
                continue

            elif checked_response == 'is location':
                # Response is a direction: N, S, W, E
                new_room = dracula_jr.get_next_room(response)
                for location in locations:
                    # Matches input to Location
                    if new_room == location.name:
                        new_room = location
                        player.set_location(new_room)

            elif checked_response == 'is command':
                # Response is a command
                no_match = -1
                result = dracula_jr.inspect_item(player.get_location(), response)
                if result is True:  # Command matches the item in location
                    if player.backpack.in_backpack(player.location.item.name) == no_match:
                        new_item = player.backpack.add(player.location.item.name)
                        for item in items:
                            if new_item == item.name:
                                new_item = item
                                print(new_item.message_picked_up)
                                player.backpack.show_inventory()
                elif result is False:   # Command does not match the item in location
                    dracula_jr.wrong_command()
                    continue

        # win or lose game
        play_again = input('Would you like to play again?')
        if play_again == 'yes':
            print('OK, here we go again.')
            continue
        else:
            print(f'No worries, {player.name}. See you next time.')
            time.sleep(3)
            quit()


if __name__ == "__main__":
    play()
