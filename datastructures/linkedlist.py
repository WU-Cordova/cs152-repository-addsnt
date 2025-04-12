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

            if not isinstance(item, data_type):
                raise TypeError("Sequence contains items of incorrect type")

            llist.append(item)

        return llist

    def append(self, item: T) -> None:
        # raise TypeError for wrong type
        # handle empty and non-empty cases
        # check that all the items in sequence are of the same type (data_type)
        if not isinstance(item, self.data_type):
            raise TypeError("Item is not the correct type")

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
        if not isinstance(item, self.data_type):
            raise TypeError("Item is not the correct type")

        new_node = LinkedList.Node(data= item)

        new_node.next = self.head

        if self.head:
            self.head.previous = new_node

        self.head = new_node

        self.count += 1


    def insert_before(self, target: T, item: T) -> None:
        if target is None:
            raise ValueError
        if not isinstance(target, self.data_type) or not isinstance(item, self.data_type):
            raise TypeError
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

        new_node = LinkedList.Node(data=item)
        new_node.next = travel
        new_node.previous = travel.previous

        if travel.previous:
            travel.previous.next = new_node
        else:
            self.head = new_node
        travel.previous = new_node
        self.count += 1


        if travel is self.head:
            self.prepend(item)
            return

        # Not the head
        


    def insert_after(self, target: T, item: T) -> None:
        if target is None:
            raise ValueError
        if not isinstance(target, self.data_type) or not isinstance(item, self.data_type):
            raise TypeError

        travel = self.head
        while travel:
            if travel.data == target:
                break
            travel = travel.next

        if travel is None:
            raise ValueError(f'The target value {target} was not found in the linked list.')

        new_node = LinkedList.Node(data=item)
        new_node.next = travel.next
        new_node.previous = travel

        if travel.next:
            travel.next.previous = new_node
        else:
            self.tail = new_node

        travel.next = new_node
        self.count += 1


        

    def remove(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError

        travel = self.head
        while travel:
            if travel.data == item:
                break
            travel = travel.next

        if travel is None:
            raise ValueError(f'The item {item} was not found in the linked list.')

        if travel.previous:
            travel.previous.next = travel.next
        else:
            self.head = travel.next

        if travel.next:
            travel.next.previous = travel.previous
        else:
            self.tail = travel.previous

        self.count -= 1


    def remove_all(self, item: T) -> None:
        if not isinstance(item, self.data_type):
            raise TypeError
        
        travel = self.head
        while travel:
            if travel.data == item:
                if travel.previous:
                    travel.previous.next = travel.next
                else:
                    self.head = travel.next

                if travel.next:
                    travel.next.previous = travel.previous
                else:
                    self.tail = travel.previous

                self.count -= 1
                
            travel = travel.next


    def pop(self) -> T:
        if self.empty:
            raise IndexError("pop from empty list")

        popped_item = self.tail.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.previous
            self.tail.next = None

        self.count -= 1
        return popped_item


    def pop_front(self) -> T:
        if self.empty:
            raise IndexError("pop from empty list")

        popped_item = self.head.data
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.previous = None

        self.count -= 1
        return popped_item


    @property
    def front(self) -> T:
        if self.head:
            return self.head.data
        else:
            raise IndexError("front from empty list")

    @property
    def back(self) -> T:
        # check that tail is not None first
        if self.tail:
            return self.tail.data
        else:
            raise IndexError("back from empty list")


    @property
    def empty(self) -> bool:
        return self.head is None

    def __len__(self) -> int:
        return self.count

    def clear(self) -> None:
        self.head = self.tail = None
        self.count = 0

    def __contains__(self, item: T) -> bool:
        if not isinstance(item, self.data_type):
            return False
        
        travel = self.head
        while travel:
            if travel.data == item:
                return True
            travel = travel.next
        return False

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
        reversed_list = LinkedList(data_type=self.data_type)
        travel = self.tail
        while travel:
            reversed_list.append(travel.data)
            travel = travel.previous
        return reversed_list


        # okay maybe not...
        '''if self.travel_node in None:
            raise StopIteration
        
        data = self.travel_node.data
        self.travel_node = self.travel_node.previous

        return data'''
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, LinkedList):
            return False
        if self.count != other.count:
            return False

        travel_self = self.head
        travel_other = other.head
        while travel_self and travel_other:
            if travel_self.data != travel_other.data:
                return False
            travel_self = travel_self.next
            travel_other = travel_other.next
        return True

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
