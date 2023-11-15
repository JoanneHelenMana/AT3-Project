class Location:

    def __init__(self, name, north_exit, south_exit, west_exit, east_exit, description, north_leads_to=None,
                 south_leads_to=None, west_leads_to=None, east_leads_to=None, visited=False, starting_point=False,
                 ending_point=False):

        self.name = name
        self.description = description
        self.north_exit = north_exit
        self.south_exit = south_exit
        self.west_exit = west_exit
        self.east_exit = east_exit
        self.visited = visited
        self.north_leads_to = north_leads_to
        self.south_leads_to = south_leads_to
        self.west_leads_to = west_leads_to
        self.east_leads_to = east_leads_to
        self.starting_point = starting_point
        self.ending_point = ending_point

    def __str__(self):
        return f'{self.name}'

    def get_available_exits(self):
        """Gets all available exits of a given location as a list (N, S, W, and/or E)."""

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

    def get_north_leads_to(self):
        return self.north_leads_to
