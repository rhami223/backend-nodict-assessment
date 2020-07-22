#!/usr/bin/env python3
"""
Implementation of the NoDict assignment
"""

__author__ = 'Ramon Hamilton with help from Howard Post'


class Node:
    """A container to store key values in a
    hashtable"""

    def __init__(self, key, value=None):
        """Init method takes key which is required
        and value which is not required"""
        self.key = key
        self.value = value
        self.hash = hash(self.key)

    def __repr__(self):
        """returns a string representation of
        Node object"""
        return f'{self.__class__.__name__}({self.key}, {self.value})'

    def __eq__(self, other):
        """Dunder method that comares key values"""
        return self.key == other.key


class NoDict:
    """A python dictionary without 
    using python methods to create dictionary"""

    def __init__(self, num_buckets=10):
        """Init method for NoDict takes in optional number
        of buckets. If no number is given defaults to 10"""
        self.buckets = [[] for _ in range(num_buckets)]
        self.size = num_buckets

    def __repr__(self):
        """Return a string representing the NoDict
        contents"""
        return '\n'.join([f'{self.__class__.__name__}.{i}:{bucket}'
                          for i, bucket in enumerate(self.buckets)])

    def add(self, key, value=None):
        """Method accepts key and value and creates a
        new node, then stores that node in a bucket."""
        new_node = Node(key, value)
        bucket = self.buckets[new_node.hash % self.size]
        for kv in bucket:
            if kv == new_node:
                bucket.remove(kv)
                break
        bucket.append(new_node)

    def get(self, key):
        """Method used to return value of key value pair.
        If key does not exist raises a KeyError"""
        key_val = Node(key)
        bucket = self.buckets[key_val.hash % self.size]
        for kv in bucket:
            if kv == key_val:
                return kv.value
        raise KeyError(f'{key} not found')

    def __getitem__(self, key):
        """Dunder method which allows you to use square
        bracket notation to look up value"""
        value = self.get(key)
        return value

    def __setitem__(self, key, value):
        """Dunder method which allows you to use square
        bracket notation to set the value of a key"""
        self.add(key, value)