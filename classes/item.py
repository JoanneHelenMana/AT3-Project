class Item:
    def __init__(self, name, message_in_location, message_picked_up):
        self.name = name
        self.message_in_location = message_in_location
        self.message_picked_up = message_picked_up

    def __str__(self):
        print(f'{self.name}')
