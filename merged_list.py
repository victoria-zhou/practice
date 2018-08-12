#!/bin/python3

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

def print_singly_linked_list(node):
    while node:
        print(node.data)
        node = node.next


def findMergeNode1(head1, head2):
    current_node1 = head1
    current_node2 = head2
    length1 = length2 = 0
    
    while current_node1:
        length1 += 1
        current_node1 = current_node1.next
        
    while current_node2:
        length2 += 1
        current_node2 = current_node2.next
    
    skip = abs(length2 - length1)
    if length1 > length2:
        current_a = head1
        current_b = head2
    else:
        current_a = head2
        current_b = head1
    
    while current_b != current_a:
        current_a = current_a.next
        if skip == 0:
            current_b = current_b.next
        else:
            skip -= 1
    return current_a.data

    # if length1 > length2:
    #     start_node1 = head1
    #     for i in range(length1-length2):
    #         start_node1 = start_node1.next
    #     start_node2 = head2
    #     while start_node1.data != start_node2.data:
    #         start_node1 = start_node1.next
    #         start_node2 = start_node2.next
    
    # elif length2 > length1:
    #     start_node2 = head2
    #     for i in range(length2-length1):
    #         start_node2 = start_node2.next
    #     start_node1 = head1
    #     while start_node1.data != start_node2.data:
    #         start_node1 = start_node1.next
    #         start_node2 = start_node2.next
    # else:
    #     start_node1 = head1
    #     start_node2 = head2
    #     while start_node1.data != start_node2.data:
    #         start_node1 = start_node1.next
    #         start_node2 = start_node2.next
    # return start_node1.data

def FindMergeNode(headA, headB):
    curA = headA
    curB = headB
    while not curA == curB:
        if curA.next is None:
            curA = headB
        else:
            curA = curA.next
        if curB.next is None:
            curB = headA
        else:
            curB = curB.next
    return curA.data

sll1 = SinglyLinkedList()
for item in [1, 2, 3, 4, 5, 6, 7]:
    sll1.insert_node(item)


sll2 = SinglyLinkedList()
for item in [-1, -2, -3, -4]:
    sll2.insert_node(item)

for item in [11, 12, 13, 14]:
    node = SinglyLinkedListNode(item)
    sll1.tail.next = node
    sll1.tail = node
    sll2.tail.next = node
    sll2.tail = node


assert FindMergeNode(sll1.head, sll2.head) == 11
assert findMergeNode1(sll1.head, sll2.head) == 11
