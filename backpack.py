class Backpack:
    """
    Backpack Class
    ToDo: [X] Instantiate backpack
    ToDo: [X] Add Item
    ToDo: [ ] Remove Item
    ToDo: [ ] List Items
    ToDo: [X] Count items
    ToDo: [ ] in backpack (Search for Item - Student to do)
    ToDo: [X] Sort Items
    """

    def __init__(self):
        self._backpack = []
        items = []
        if type(items) is not "<class 'list'>":
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
        self._backpack.sort()

    def count(self):
        return self._backpack.count()

    def list(self):
        for item in self._backpack:
            print(item)

    def add(self, item):
        if item is not None:
            self._backpack.append(item)
            self.sort()

    def in_backpack(self, item):
        """
        Complete this method using a binary search
        returns -1 or False if not found
        returns position if found
        :param item:
        :return: -1 | False | integer
        """
        return None
