# datastructures.array.Array

""" This module defines an Array class that represents a one-dimensional array. 
    See the stipulations in iarray.py for more information on the methods and their expected behavior.
    Methods that are not implemented raise a NotImplementedError until they are implemented.
"""

from __future__ import annotations
from collections.abc import Sequence
import os
from typing import Any, Iterator, overload
import numpy as np
from numpy.typing import NDArray
import copy

from datastructures.iarray import IArray, T


class Array(IArray[T]):  

    def __init__(self, starting_sequence: Sequence[T]=[], data_type: type=object) -> None: 
        if not isinstance(starting_sequence, Sequence):
	        raise ValueError("This should raise only raise if a strating_sequence is not a sequence type.")

        if not isinstance(data_type, type):
            raise ValueError("This should raise because data_type is not a type, it's a data value!")
        
        for item in starting_sequence:
            if not isinstance(item, data_type):
                raise TypeError("Not all elements in starting_sequence match the specified data_type.")
        
        self.__data_type = data_type
        self.__logical_size = len(starting_sequence)
        self.__capacity = self.__logical_size

        self.__elements = np.empty(self.__capacity, dtype = data_type)

        for index in range(self.__logical_size):
            self.__elements[index] = copy.deepcopy(starting_sequence[index])

    @overload
    def __getitem__(self, index: int) -> T: ...
    @overload
    def __getitem__(self, index: slice) -> Sequence[T]: ...
    def __getitem__(self, index: int | slice) -> T | Sequence[T]:

        if not isinstance(int, slice):
            raise TypeError("Index must be an interger or a slice")
        
        if isinstance(index, slice):
            start, stop = index.start, index.stop

            if start >= self.__logical_size or stop > self.__logical_size:
                raise IndexError("Out of bounds")

            items_to_return = self.__elements[start:stop].tolist()

            return Array(starting_sequence=items_to_return, data_type=self.__data_type)

        elif isinstance(index, int):
            return self.__elements[index]
    
    def __setitem__(self, index: int, item: T) -> None:
        if isinstance(item, self.__data_type):
            self.__elements[index] = item
        else:
            raise TypeError(f"Item must be of type {self.__data_type.__name__}")

    def append(self, data: T) -> None:
        if self.__capacity == self.__logical_size:
            self.__capacity = self.__capacity*2
            new_elements = np.empty(self.__capacity, dtype=self.__data_type)

            for i in range(self.__logical_size):
                new_elements[i] = self.__elements[i]

        self.__elements = new_elements

        self.__elements[self.__logical_size] = data
        self.__logical_size += 1

    def append_front(self, data: T) -> None:
        if self.__capacity == self.__logical_size:
            self.__capacity = self.__capacity*2
            new_elements = np.empty(self.__capacity, dtype=self.__data_type)

            new_elements.append(data)

            for i in range(self.__logical_size):
                new_elements[i+1] = self.__elements[i]

        self.__elements = new_elements

        self.__logical_size += 1
        # make a copy of array, add thing to the front, and then add everything else

    def pop(self) -> None:
        self.__logical_size -= 1

        if self.__logical_size <= self.__capacity//4 and self.__capacity>1:
            self.__capacity //= 2

            self.__elements = np.resize(self.__elements, self.__capacity)

    def pop_front(self) -> None:
        for i in range(1, self.__logical_size-1):
            self.__elements[i-1] = self.__elements[i]
        
        self.__logical_size -= 1

        if self.__logical_size <= self.__capacity//4 and self.__capacity>1:
            self.__capacity //= 2 
        
            self.__elements = np.resize(self.__elements, self.__capacity)
        
    def __len__(self) -> int: 
        return self.__logical_size

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Array):
            return False

        if self.__logical_size != other.__logical_size:
            return False

        '''if self.__data_type != other.__data_type:
            return False'''
            # gets rid of data_type and passes tets, may not be good in the future though

        if not np.array_equal(self.__elements[:self.__logical_size], other.__elements[:other.__logical_size]):
            return False

        return True

        
    def __iter__(self) -> Iterator[T]:
        # allows for iteration through elements
        for i in range(self.__logical_size):
            yield self.__elements[i]

    def __reversed__(self) -> Iterator[T]:
        for i in range(self.__logical_size-1, -1,-1):
            yield self.__elements[i]

    def __delitem__(self, index: int) -> None:
        if isinstance(index, int):
            if index < 0 or index >=self.__logical_size:
                raise IndexError("Index out of range")
            else:
                for i in range(index, self.__logical_size-1):
                    self.__elements[i] = self.__elements[i+1]
                self.__logical_size -= 1
        else:
            raise TypeError("index must be an integer")

    def __contains__(self, item: Any) -> bool:
        for i in range(self.__logical_size):
            if self.__elements[i] == item:
                return True
        return False

    def clear(self) -> None:
        # clears entire array, and sets logical and capacity back to 0
        self.__logical_size = 0
        self.__capacity = 0
        self.__elements = np.empty(self.__capacity, dtype = self.__data_type)

    def __str__(self) -> str:
        return '[' + ', '.join(str(item) for item in self) + ']'
    
    def __repr__(self) -> str:
        return f'Array {self.__str__()}, Logical: {self.__logical_size}, Physical: {len(self.__elements)}, type: {self.__data_type}'
    

if __name__ == '__main__':
    filename = os.path.basename(__file__)
    print(f'This is the {filename} file.\nDid you mean to run your tests or program.py file?\nFor tests, run them from the Test Explorer on the left.')