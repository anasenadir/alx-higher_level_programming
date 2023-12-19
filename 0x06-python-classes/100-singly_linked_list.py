#!/usr/bin/python3
"""Define classes for a singly-linked list."""



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
        """Get/set the next_node of the Node."""
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

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
