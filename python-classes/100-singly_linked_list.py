#!/usr/bin/python3

"""
This module defines a Node class and a SinglyLinkedList class
to create and manage a sorted singly linked list of integers.
"""


class Node:
    """Represents a node of a singly linked list."""

    def __init__(self, data, next_node=None):
        """
        Initialize a new node.

        Args:
            data (int): The data value for the node.
            next_node (Node or None): The next node in the list.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Retrieve the data value of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        """
        Set the data value of the node.

        Args:
            value (int): The new data value.

        Raises:
            TypeError: If value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Retrieve the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Set the next node reference.

        Args:
            value (Node or None): The new next node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """Defines a singly linked list of Node objects in sorted order."""

    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.__head = None  # start with empty list

    # insert the new_node
    def sorted_insert(self, value):
        """
        Insert a new Node into the list in increasing sorted order.

        Args:
            value (int): The data value to insert.
        """
        new_node = Node(value)

        # if empty list or new node should be first
        if self.__head is None or value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return

        # insert new node in the middle, traverse to find the correct spot
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node

        new_node.next_node = current.next_node
        current.next_node = new_node

    # make the list printable:
    def __str__(self):
        """
        Return a string representation of the list,
        with one node's data per line.
        """
        result = []
        current = self.__head
        # traverse through the linked list
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
