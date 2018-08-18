from collections import deque

class Node:
    def __init__(self, data=None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = Node()

    def insert_node(self, root, data):
        if not root:
            return Node(data)
        else:
            if data >= root.data:
                current_node = self.insert_node(root.right, data)
                root.right = current_node 
            else:
                current_node = self.insert_node(root.left, data)
                root.left = current_node 
        return root

    def print(self, root):
        result = []
        queue = []
        if root:
            queue.append(root)
            while queue:
                current_node = queue.pop(0) # if pop(), it removes and returns the last item in the list
                result.append(current_node.data)
                if current_node.left:
                    queue.append(current_node.left)
                if current_node.right:
                    queue.append(current_node.right)
        print(' '.join(map(str, result))) # know how to use join() and map() 


aTree = BinaryTree()
root = None
root = aTree.insert_node(root, 5)
root = aTree.insert_node(root, 6)
root = aTree.insert_node(root, 7)
root = aTree.insert_node(root, 8)
root = aTree.insert_node(root, 9)
root = aTree.insert_node(root, 2)

aTree.print(root)