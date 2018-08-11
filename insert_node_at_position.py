import math
import os
import random
import re
import sys

class SingleLinkedListNode:
    def __init__(self,data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'{self.data}:{self.next}'

class SingleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def append(self, data):
        node = SingleLinkedListNode(data)
        if self.head == None:
            self.head = node 
            self.tail = node
        self.tail.next = node
        self.tail = node

    # def display(self):
    #     node = self.head
    #     while node != None:
    #         print(node) 
    #         node = node.next
    #     print(node) 

    def __repr__(self):
        data = []
        node = self.head
        while node:
            data.append(node.data)
            node = node.next
        return f'{data}'

def insert_node_at_position(head, pos, data):
    new_node = SingleLinkedListNode(data)
    if pos == 0:
        new_node.next= head
        head = new_node
    else:
        current_position = 0
        current_node = head
        while current_position != pos-1:
            current_position += 1
            current_node = current_node.next

        new_node.next = current_node.next  
        current_node.next = new_node

    return head


linked_list = SingleLinkedList()
linked_list.append(4)
linked_list.append(5)
linked_list.append(6)
linked_list.append(6)

#linked_list.display()
print(linked_list)

print(insert_node_at_position(linked_list.head, 1, 1))

