import math
import os
import random
import re
import sys

class SinglyLinkedListNode:
    def __init__(self, node_data):
        self.data = node_data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_node(self, node_data):
        node = SinglyLinkedListNode(node_data)

        if not self.head:
            self.head = node
        else:
            self.tail.next = node
        self.tail = node

        return node 

def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next

def has_circle(head):
    if head == None:
        return False

    current_node = head
    data = set()
    while current_node.next:
        if id(current_node) in data: # id returns the memory address of an unique object
            return True
        else:
            data.add(id(current_node)) # know how to use id
            current_node = current_node.next
    return False

    # below method only applies to nodes that have unique data, will fail if same data occurs more than once
    # while current_node.next:     
    #     if current_node.data in data:
    #         return True
    #     else:
    #         data.add(current_node.data)
    #         current_node = current_node.next
    # return False

linked_list1 = SinglyLinkedList()
node = linked_list1.insert_node(2) #insert_node returns node, thus node == memories this node for below use, node != node.data, here 2
linked_list1.insert_node(3)
linked_list1.insert_node(6)
node2 = linked_list1.insert_node(7)
node2.next = node

linked_list2 = SinglyLinkedList()
linked_list2.insert_node(2)
linked_list2.insert_node(3)
linked_list2.insert_node(6)
linked_list2.insert_node(7)

linked_list3 = SinglyLinkedList()
linked_list3.insert_node(2)
linked_list3.insert_node(2)
linked_list3.insert_node(2)
linked_list3.insert_node(2)


assert has_circle(linked_list1.head) == True
assert has_circle(linked_list2.head) == False
assert has_circle(linked_list3.head) == False
