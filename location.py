class Location:

    def __init__(self, name, north_exit, south_exit, west_exit, east_exit,
                 starting_point=False, ending_point=False):
        self.name = name
        self.north_exit = north_exit
        self.south_exit = south_exit
        self.west_exit = west_exit
        self.east_exit = east_exit

    def __str__(self):
        return f'{self.name}'
