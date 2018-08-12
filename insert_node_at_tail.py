import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

    def __repr__(self):
        return f'{self.data}:{self.next}'

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        node = SinglyLinkedListNode(data)
        if self.head == None:
            self.head = node 
            self.tail = node
        self.tail.next = node
        self.tail = node

    def __repr__(self):
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next
        return f'{data}'

def print_singly_linked_list(node, sep, fptr):
    while node:
        fptr.write(str(node.data))

        node = node.next

        if node:
            fptr.write(sep)

def insertNodeAtTail(head, data):
    new_node = SinglyLinkedListNode(data)
    curr_node = head
    while curr_node.next:
        curr_node = curr_node.next
    curr_node.next = new_node
    return head


llist = SinglyLinkedList()
llist.append(5)
llist.append(2)
llist.append(2)
llist.append(1)

print(llist)
print(insertNodeAtTail(llist.head, 6))
print(insertNodeAtTail(llist.head, 0))

