from location import Location


class Map:
    """."""
    def __init__(self):
        self._map_array = []
        file_name = "map.txt"
        self.create_map_file(file_name)
        self.create_map()

    @staticmethod
    def create_map_file(file):
        """Creates the map file."""
        try:
            open(file, "x")
        except FileExistsError:
            pass

    def create_map(self):
        """
        Develop.

        >>> create_map()
        [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]
        """
        rows, cols = (3, 3)
        self._map_array = [['_' for i in range(cols)] for j in range(rows)]
        return self._map_array

    def print_map(self):
        """
        Prints the castle map.

        '_' = not visited
        'X' = visited
        ' ' = no room is accessible
        """

        # arr[0][0] = 1
        for row in self._map_array:
            for element in row:
                print(element, end=" ")
            print()
