from typing import Iterable, Optional
from datastructures.ibag import IBag, T


class Bag(IBag[T]):
    def __init__(self, *items: Optional[Iterable[T]]) -> None:
        self.items = []
        if items:
            for item in items:
                self.add(item)

    def add(self, item: T) -> None:
        if item is None:
            raise TypeError("You cannot add nothing to the bag")
        self.items.append(items)

    def remove(self, item: T) -> None:
        if item not in self.items:
            raise ValueError("That item is not in the bag")
        self.items.remove(item)

    def count(self, item: T) -> int:
        return self.items.count(item)

    def __len__(self) -> int:
        return len(self.items)

    def distinct_items(self) -> int:
        distinct_items = set(self.items)
        return distinct_items

    def __contains__(self, item) -> bool:
        if item in items:
            return True
        else:
            return False

    def clear(self) -> None:
        self.items.clear()