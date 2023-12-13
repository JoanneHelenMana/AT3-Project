class Backpack:
    """The player's backpack contains all items the player picks up on their way around the castle."""
    def __init__(self):
        self._backpack = []
        items = []
        if type(items) != "<class 'list'>":
            items = []
        for item in items:
            self._backpack.append(item)
        self.sort()

    def __str__(self):
        """Prints backpack creation status."""
        if type(self._backpack) is list:
            message = "Backpack was created successfully."
        else:
            message = "Backpack not created."
        return message

    def sort(self):
        """Sorts items in backpack."""
        self._backpack.sort()

    def count(self):
        """Counts all items in the backpack."""
        return self._backpack.count(self)

    def show_inventory(self):
        """Prints backpack's inventory."""
        print('Inventory: ')
        item_str = ""
        for item in self._backpack:
            item_str = ', '.join(self._backpack)
        print(item_str)

    def add(self, item):
        """Adds items to the backpack."""
        if item is not None:
            self._backpack.append(item)
            self.sort()
            return item

    def in_backpack(self, item):
        """
        Searches whether an item is already in the backpack.
        It returns -1 if not found, and returns position if found.

        :param item: item
        :return: -1 | integer
        """
        low = 0
        high = len(self._backpack) - 1
        mid = 0

        while low <= high:
            self.sort()
            mid = (high + low) // 2

            if self._backpack[mid] < item:
                low = mid + 1

            elif self._backpack[mid] > item:
                high = mid - 1

            else:
                return mid  # Item present at position 'mid'

        return -1   # Item not in backpack
