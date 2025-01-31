from collections.abc import Iterable, Iterator
from typing import Any, List


class OrderIterator(Iterator):
    _position: int = None
    _reverse: bool = False

    def __init__(self, collection, reverse=False):
        self._collection = collection
        self._reverse = reverse
        self._position = -1 if reverse else 0

    def __next__(self):
        try:
            value = self._collection[self._position]
            self._position += -1 if self._reverse else 1
        except IndexError:
            raise StopIteration()
        return value


class WordsCollection(Iterable):
    def __init__(self, collection: List[Any] | None = None):
        self._collection = collection or []

    def __getitem__(self, index: int) -> Any:
        return self._collection[index]

    def __iter__(self) -> OrderIterator:
        return OrderIterator(self._collection)

    def get_reverse_iterator(self) -> OrderIterator:
        return OrderIterator(self._collection, True)

    def add_item(self, item):
        self._collection.append(item)


# Usage
words_collection = WordsCollection()
words_collection.add_item("Apple")
words_collection.add_item("Banana")
words_collection.add_item("Pineapple")
words_collection.add_item("Cat")

print("Straight traversal:")
for item in words_collection:
    print(item)

print("\nReverse traversal:")
for item in OrderIterator(words_collection, reverse=True):
    print(item)

# the caller does not need to know the iterator's type
print("\nReverse traversal:")
for item in words_collection.get_reverse_iterator():
    print(item)
