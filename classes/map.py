class Map:
    """."""
    def __init__(self):
        self._map_array = []
        self.file_name = "map.txt"
        self.create_file()
        self.create_map()

    def create_file(self):
        """Creates the map file."""
        try:
            open(self.file_name, "x")
        except FileExistsError:
            pass

    def create_map(self):
        """
        Creates the initial map array and saves it to file.
        """
        rows, cols = (3, 3)
        self._map_array = [['_' for i in range(cols)] for j in range(rows)]     # updates array variable
        # print(f'array: {self._map_array}')
        self.update_file()  # updates text file

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
        pass
