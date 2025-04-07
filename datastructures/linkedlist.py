from __future__ import annotations

from dataclasses import dataclass
import os
from typing import Optional, Sequence
from datastructures.ilinkedlist import ILinkedList, T


class LinkedList[T](ILinkedList[T]):

    @dataclass
    class Node:
        data: T
        next: Optional[LinkedList.Node] = None
        previous: Optional[LinkedList.Node] = None

    def __init__(self, data_type: type = object) -> None:
        self.count = 0
        self.head: Optional[LinkedList.Node]= None
        self.tail: Optional[LinkedList.Node]= None
        self.data_type = data_type

    @staticmethod
    def from_sequence(sequence: Sequence[T], data_type: type=object) -> LinkedList[T]:
        # check that all the items in sequence are of the same type (data_type)

        llist: LinkedList[T] = LinkedList(data_type=data_type)

        for item in sequence:
            llist.append(item)

        return llist

    def append(self, item: T) -> None:
        # raise TypeError for wrong type
        # handle empty and non-empty cases
        # check that all the items in sequence are of the same type (data_type)

        node = LinkedList.Node(data=item)

        if self.empty:
            self.head = self.tail = node

        else: 
            # set node's previous to current tail
            node.previous = self.tail

            # set tail's next to new node
            if self.tail:
                self.tail.next = node

            # set tail to new node
            self.tail = node
        
        self.count += 1

    def prepend(self, item: T) -> None:
        # check that item is the same type (data_type)
        
        new_node = LinkedList.Node(data= item)

        new_node.next = self.head

        if self.head:
            self.head.previous = new_node

        self.head = new_node

        self.count += 1


    def insert_before(self, target: T, item: T) -> None:
        # Rise ValueError if the target does not exist
        # Raise TypeError if the target is not the right type
        # Raise TypeError if the item is not the right type


        travel = self.head

        while travel:

            if travel.data == target:
                break

            travel = travel.next

        if travel is None:
            raise ValueError(f'The target value {target} was not found in the linked list.')

        if travel is self.head:
            self.prepend(item)
            return

        # Not the head
        


    def insert_after(self, target: T, item: T) -> None:
        raise NotImplementedError("LinkedList.insert_after is not implemented")

    def remove(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove is not implemented")

    def remove_all(self, item: T) -> None:
        raise NotImplementedError("LinkedList.remove_all is not implemented")

    def pop(self) -> T:
        raise NotImplementedError("LinkedList.pop is not implemented")

    def pop_front(self) -> T:
        raise NotImplementedError("LinkedList.pop_front is not implemented")

    @property
    def front(self) -> T:
        raise NotImplementedError("LinkedList.front is not implemented")

    @property
    def back(self) -> T:
        # check that tail is not None first
        if self.tail:
            return self.tail.data

    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        raise NotImplementedError("LinkedList.clear is not implemented")

    def __contains__(self, item: T) -> bool:
        raise NotImplementedError("LinkedList.__contains__ is not implemented")

    def __iter__(self) -> ILinkedList[T]:
        self.travel_node = self.head
        return self

    def __next__(self) -> T:
        if self.travel_node is None:
            raise StopIteration

        data = self.travel_node.data
        self.travel_node = self.travel_node.next

        return data


    def __reversed__(self) -> ILinkedList[T]:
        # okay maybe not...
        if self.travel_node in None:
            raise StopIteration
        
        data = self.travel_node.data
        self.travel_node = self.travel_node.previous

        return data
    
    def __eq__(self, other: object) -> bool:
        raise NotImplementedError("LinkedList.__eq__ is not implemented")

    def __str__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return '[' + ', '.join(items) + ']'

    def __repr__(self) -> str:
        items = []
        current = self.head
        while current:
            items.append(repr(current.data))
            current = current.next
        return f"LinkedList({' <-> '.join(items)}) Count: {self.count}"


if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'OOPS!\nThis is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')
