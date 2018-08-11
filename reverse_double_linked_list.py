import math
import os
import random
import re
import sys

class DoublyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None
        self.prev = None

    def __repr__(self): #master this
        return f'{self.data}:{self.next}'

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert_node(self, node_data):
        node = DoublyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
            node.prev = self.tail


        self.tail = node

    def __repr__(self): # master this
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next
        return f'{data}'

def print_doubly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def reverse(head):
    abstracted_list = []
    current_node = head
    while current_node:
        abstracted_list.append(current_node.data)
        current_node = current_node.next
    
    linked_list = DoublyLinkedList()
    for i in range(len(abstracted_list)-1, -1, -1):
        linked_list.insert_node(abstracted_list[i])
    
    return linked_list.head

new_linked_list = DoublyLinkedList()
new_linked_list.insert_node(1)
new_linked_list.insert_node(5)
new_linked_list.insert_node(6)
new_linked_list.insert_node(2)


print(reverse(new_linked_list.head))