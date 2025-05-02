import copy
from typing import Callable, Iterator, Optional, Tuple
from datastructures.ihashmap import KT, VT, IHashMap
from datastructures.array import Array
import pickle
import hashlib

from datastructures.linkedlist import LinkedList

class HashMap(IHashMap[KT, VT]):

    def __init__(self, number_of_buckets=7, load_factor=0.75, custom_hash_function: Optional[Callable[[KT], int]]=None) -> None:
        self._buckets: Array[LinkedList[Tuple[KT, VT]]] = \
            Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(number_of_buckets)], \
                data_type=LinkedList)
        self._count: int = 0
        self._load_factor_threshold: float = load_factor
        self._hash_function = custom_hash_function or self._default_hash_function

    def _get_bucket_number(self, key: KT) -> int:
        return self._default_hash_function(key) % len(self._buckets)


    def __getitem__(self, key: KT) -> VT:
        bucket_index: int = self._get_bucket_number(key)
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]
        for k, v in bucket_chain:
            if k == key:
                return v
        raise KeyError(key)


    def __setitem__(self, key: KT, value: VT) -> None:        
        bucket_index: int = self._get_bucket_number(key)
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]
        current = bucket_chain.head
        while current:
            k, v = current.data
            if k == key:
                current.data = (key, value)
                return
            current = current.next

        bucket_chain.append((key, value))
        self._count += 1
        if self._count / len(self._buckets) > self._load_factor_threshold:
            self._resize(self.next_prime_after_double(len(self._buckets)))


    def keys(self) -> Iterator[KT]:
        for bucket in self._buckets:
            for key, _ in bucket:
                yield key
    
    def values(self) -> Iterator[VT]:
        for bucket in self._buckets:
            for _, value in bucket:
                yield value

    def items(self) -> Iterator[Tuple[KT, VT]]:
        for bucket in self._buckets:
            for item in bucket:
                yield item
            
    def __delitem__(self, key: KT) -> None:
        bucket_index: int = self._get_bucket_number(key)
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]
        found = False
        for k, v in bucket_chain:
            if k == key:
                bucket_chain.remove((k, v))
                self._count -= 1
                found = True
                break  # Assuming you only want to delete the first occurrence of the key
        if not found:
            raise KeyError(key)

    
    def __contains__(self, key: KT) -> bool:
        # 1. compute the bucket based on key
        bucket_index: int = self._get_bucket_number(key)

        # 2. get the bucket chains in that bucket
        bucket_chain: LinkedList[tuple] = self._buckets[bucket_index]

        # 3. is there a tuple with the key in it?
        for (k, v) in bucket_chain:
            if k == key:
                return True

        return False
        
    def __len__(self) -> int:
        return self._count
    
    def __iter__(self) -> Iterator[KT]:
        yield from self.keys()
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, HashMap):
            return False
        if len(self) != len(other):
            return False
        for key, value in self.items():
            if key not in other or other[key] != value:
                return False
        return True


    def __str__(self) -> str:
        return "{" + ", ".join(f"{key}: {value}" for key, value in self) + "}"
    
    def __repr__(self) -> str:
        return f"HashMap({str(self)})"

    def _resize(self, new_capacity: int) -> None:
        old_buckets = self._buckets
        self._buckets = Array(starting_sequence=[LinkedList(data_type=tuple) for _ in range(new_capacity)], data_type=LinkedList)
        self._count = 0
        for bucket in old_buckets:
            for key, value in bucket:
                self[key] = value


    @staticmethod
    def next_prime_after_double(n):

        def is_prime(num: int) -> bool:
            if num < 2:
                return False
            for i in range(2, int(num**0.5)+1): # sqrt of num = num**1/2
                if num % i == 0:
                    return False
            return True

        next_prime = n * 2

        while not is_prime(next_prime):
            next_prime += 1

        return next_prime



    @staticmethod
    def _default_hash_function(key: KT) -> int:
        """
        Default hash function for the HashMap.
        Uses Pickle to serialize the key and then hashes it using SHA-256. 
        Uses pickle for serialization (to capture full object structure).
        Falls back to repr() if the object is not pickleable (e.g., open file handles, certain C extensions).
        Returns a consistent integer hash.
        Warning: This method is not suitable
        for keys that are not hashable or have mutable state.

        Args:
            key (KT): The key to hash.
        Returns:
            int: The hash value of the key.
        """
        try:
            key_bytes = pickle.dumps(key)
        except Exception:
            key_bytes = repr(key).encode()
        return int(hashlib.md5(key_bytes).hexdigest(), 16)