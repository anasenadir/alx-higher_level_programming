#!/usr/bin/python3
"""Node Class"""


from typing import Any


class Node:
    """Node Class Of Singly linked list"""

    def __init__(self, data, next_node=None):
        """initialize the Node"""
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the value of data prop"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value to the data

        Args:
            data (int): data must be an integer

        Raises:
            TypeError: if the value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("next_node must be a Node object")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set The the next_node value

        Args:
            value (Node): The next node

        Raises:
            TypeError: if the Type of the value is not Node and None
        """
        if (not isinstance(value, Node) and value is not None):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


"""SinglyLinkedList class"""


class SinglyLinkedList:
    """a SinglyLinkedList class that defines a singly linked list"""
    def __init__(self):
        self.__head = None

    def __str__(self) -> str:
        """return a string represinting a linkedlist"""
        current = self.__head
        linked_list_str = ""
        while(current):
            linked_list_str += str(current.data)
            if (current.next_node is not None):
                linked_list_str += "\n"
            current = current.next_node
        return linked_list_str

    def sorted_insert(self, value):
        """insert a new value to its specific location in order maner

        Args:
            value (int): the value of the new_node
        """
        new_Node = Node(value)

        if (self.__head is not None):
            self.__head = new_Node
            return

        current = self.__head
        if (current.data >= value):
            new_Node.next_node = current
            self.__head = new_Node
            return

        while (current.next_node):
            if (current.next_node.data >= value):
                new_Node.next_node = current.next_node
                current.next_node = new_Node
                return
            current = current.next_node

        current.next_node = new_Node
