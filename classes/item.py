from character import Character


class Item(Character):
    def __init__(self, name, location, message_in_location, message_picked_up):
        self.name = name
        self.location = location
        self.message_in_location = message_in_location
        self.message_picked_up = message_picked_up

