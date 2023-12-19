#!/usr/bin/python3
"""Define classes for a singly-linked list."""


class Node:
    """Node Class Of Singly linked list"""

    def __init__(self, data, next_node=None):
        """Initialize a new Node.

        Args:
            data (int): The data of the new Node.
            next_node (Node): The next node of the new Node.
        """
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
            raise TypeError("data must be a Node object")
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


class SinglyLinkedList:
    """a SinglyLinkedList class that defines a singly linked list"""
   
    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def __str__(self) -> str:
        """return a string represinting a linkedlist"""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.

        The node is inserted into the list at the correct
        ordered numerical position.

        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new
