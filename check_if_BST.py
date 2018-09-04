

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def __init__(self, data):
        self.root = Node(data)

    def add_node(self, data):
        if self.root == None:
            self.root = Node(data)
        elif data > self.root.data:
            self.root.right = Node(data)
        else:
            self.root.left = Node(data)

import sys
def bst_helper(root, min_value, max_value):
    return (root is None or (root.data < max_value and root.data > min_value and bst_helper(root.left, min_value, root.data) and bst_helper(root.right, root.data, max_value)))

def check_BST(root):
    return bst_helper(root, -float('inf'), float('inf'))


tree1 = BST(1)
for data in (2, 3, 4, 5, 6, 7):
    tree1.add_node(data)
print(check_BST(tree1.root))

tree2 = BST(1)
for data in (2, 4, 3, 5, 6, 7):
    tree2.add_node(data)
print(check_BST(tree2.root))

tree3 = BST(1)
for data in (2, 2, 4, 5, 6, 7):
    tree3.add_node(data)
print(check_BST(tree3.root))

