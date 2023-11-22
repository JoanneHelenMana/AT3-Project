import os


class Map:
    """."""
    def __init__(self, inaccessible_locations):
        self.inaccessible_locations = inaccessible_locations
        self._map_array = []
        self.file_name = "map.txt"
        self.create_file()
        self.create_map(inaccessible_locations)

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

        room_not_accessible = ' '
        for coordenate in inaccessible_locations:
            index = coordenate.split(',', 2)
            self._map_array[int(index[0])][int(index[1])] = room_not_accessible
        # print(f'array: {self._map_array}')
        self.update_file()  # updates text file
        self.print_map()    # to be removed

    def update_file(self):
        """Updates map text file (map.txt)."""
        flat_map = []
        for row in self._map_array:
            for element in row:
                flat_map.append(element)
            flat_map.append('\n')

        map_string = "".join(flat_map)
        # print(f'map string:\n{map_string}')

        with open(self.file_name, 'w+') as file:
            file.writelines(map_string.rstrip('\n'))

        with open(self.file_name, 'r') as file:
            # print('file:')
            lines = file.readlines()
            #for line in lines:
                # print(line, end='')

    def print_map(self):
        """
        Prints the castle map.

        '_' = not visited
        'X' = visited
        ' ' = room is not accessible
        """
        # arr[0][0] = 1
        for row in self._map_array:
            for element in row:
                print(element, end=" ")
            print()

    def update_map(self, row, column):
        """."""
        visited = 'X'
