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
    def __repr__(self):
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


    def __repr__(self):
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next
        return f'{data}'

def sorted_insert(head, data):
    new_node = DoublyLinkedListNode(data)
    if head.data == None:
        head = new_node
        head.next = None
    
    elif head.data > data:
        new_node.next = head 
        head.prev = new_node
        head = new_node     
    else: 
        current_node = head
        while current_node.next != None and current_node.data < data:
            current_node = current_node.next
        
        if current_node.next == None and current_node.data < data:
            current_node.next = new_node
            new_node.prev = current_node
        else:
            new_node.next = current_node
            current_node.prev.next = new_node
            current_node.prev = new_node 
            new_node.prev = current_node.prev

    return head



linked_list = DoublyLinkedList()
linked_list.insert_node(2)
linked_list.insert_node(4)
linked_list.insert_node(6)
linked_list.insert_node(10)


print(sorted_insert(linked_list.head, 5))

# assert sorted_insert(linked_list.head, 1) == 1
# assert sorted_insert(linked_list.head, 11) == 2
# assert sorted_insert(linked_list.head, 8) == 2
