#!/usr/bin/python3
""" creating an empty class that define a singly linked list"""


class Node:
    """ define a Node"""
    def __init__(self, data, next_node=None):
        """ initializing private  attribute data"""
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """ getter method just return the attribute"""
        return self.__data

    @data.setter
    def data(self, value):
        """ setter method"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """ getter method just return the attribute"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """ setter method"""
        if not (value is None or isinstance(value, Node)):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """ define a SinglyLinkedList"""
    def __init__(self):
        """ initialize a new SinglyLinkedList"""
        self.head = None

    def __str__(self):
        """ print the SinglyLinkedList"""
        current = self.head
        string = ""
        while current:
            string += str(current.data) + "\n"
            current = current.next_node
        return string.rstrip("\n")

    def sorted_insert(self, value):
        """ insert a new Node to the SinglyLinkedList"""
        new_node = Node(value)

        if self.head is None or value < self.head.data:
            new_node.next_node = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next_node is not None and\
                    current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node
