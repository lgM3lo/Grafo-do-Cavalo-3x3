class Bag:
    def __init__(self):
        self._items = []

    def add(self, item):
        self._items.append(item)

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0

    def __iter__(self):
        return iter(self._items)
