class Location:

    def __init__(self, name, north_exit, south_exit, west_exit, east_exit, description, visited=False,
                 starting_point=False, ending_point=False):
        self.name = name
        self.description = description
        self.north_exit = north_exit
        self.south_exit = south_exit
        self.west_exit = west_exit
        self.east_exit = east_exit
        self.visited = visited

    def __str__(self):
        return f'{self.name}'

    def get_available_exits(self):
        exits = []

        if self.north_exit is True:
            exits.append("N")
        if self.south_exit is True:
            exits.append("S")
        if self.west_exit is True:
            exits.append("W")
        if self.east_exit is True:
            exits.append("E")

        return exits
