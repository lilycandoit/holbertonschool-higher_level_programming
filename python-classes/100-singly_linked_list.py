#!/usr/bin/python3

class Node:
    __data = 0

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ define a linked list """

    def __init__(self):
        self.__head = None  # start with empty list

    # insert the new_node
    def sorted_insert(self, value):
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
        result = []
        current = self.__head
        # traverse through the linked list
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
