import os


class Map:
    """
    A 3x3 map.

    '_' = not visited
    'X' = visited
    ' ' = room is not accessible
    """

    def __init__(self):
        inaccessible_map_positions = ["1,0", "2,2"]
        self._map_array = []
        self.file_name = "map.txt"
        self.create_file()
        self.create_map(inaccessible_map_positions)

    def create_file(self):
        """Creates the map file."""
        if os.path.exists(self.file_name):
            os.remove(self.file_name)
        try:
            open(self.file_name, "x")
        except FileExistsError:
            pass

    def create_map(self, inaccessible_locations):
        """Creates the initial map array and saves it to file."""
        rows, cols = (3, 3)
        self._map_array = [['_' for i in range(cols)] for j in range(rows)]     # updates array variable

        if inaccessible_locations is not None:
            room_not_accessible = ' '
            for coordenate in inaccessible_locations:
                index = coordenate.split(',', 2)
                self._map_array[int(index[0])][int(index[1])] = room_not_accessible

        self.update_file()

    def update_file(self):
        """Updates map text file (map.txt)."""
        flat_map = []
        for row in self._map_array:
            for element in row:
                flat_map.append(element)
            flat_map.append('\n')

        map_string = "".join(flat_map)

        with open(self.file_name, 'w+') as file:
            file.writelines(map_string.rstrip('\n'))

        with open(self.file_name, 'r') as file:
            lines = file.readlines()

    def print_map(self):
        """Prints the castle map."""
        for row in self._map_array:
            for element in row:
                print(element, end=" ")
            print()

    def update_map(self, location):
        """."""
        visited = 'X'
        coordenate = location.map_position
        index = coordenate.split(',', 2)
        self._map_array[int(index[0])][int(index[1])] = visited
        self.update_file()
